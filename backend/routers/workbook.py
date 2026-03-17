"""Workbook CRUD — local SQLite storage for CIO homework assignments."""

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from workbook_schemas import WORKBOOK_SECTIONS

DB_PATH = Path(__file__).parent.parent / "workbook.db"

router = APIRouter(prefix="/api/workbook", tags=["workbook"])


def _get_db() -> sqlite3.Connection:
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute(
        """CREATE TABLE IF NOT EXISTS workbook_responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lecture_num INTEGER NOT NULL,
            section_key TEXT NOT NULL,
            data TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            UNIQUE(lecture_num, section_key)
        )"""
    )
    conn.row_factory = sqlite3.Row
    return conn


class WorkbookSave(BaseModel):
    data: Any


@router.get("/schemas")
def get_schemas():
    """Return all workbook form definitions."""
    return WORKBOOK_SECTIONS


@router.get("/progress")
def get_progress():
    """Return which lectures have saved data."""
    db = _get_db()
    rows = db.execute(
        "SELECT DISTINCT lecture_num FROM workbook_responses"
    ).fetchall()
    db.close()
    completed = [r["lecture_num"] for r in rows]
    return {"completed": completed, "total": len(WORKBOOK_SECTIONS)}


@router.get("")
def get_all():
    """Return all saved workbook data."""
    db = _get_db()
    rows = db.execute(
        "SELECT lecture_num, section_key, data, updated_at FROM workbook_responses ORDER BY lecture_num"
    ).fetchall()
    db.close()
    result = {}
    for r in rows:
        ln = r["lecture_num"]
        if ln not in result:
            result[ln] = {}
        result[ln][r["section_key"]] = {
            "data": json.loads(r["data"]),
            "updated_at": r["updated_at"],
        }
    return result


@router.get("/{lecture_num}")
def get_lecture(lecture_num: int):
    """Return all saved data for a lecture."""
    db = _get_db()
    rows = db.execute(
        "SELECT section_key, data, updated_at FROM workbook_responses WHERE lecture_num = ?",
        (lecture_num,),
    ).fetchall()
    db.close()
    result = {}
    for r in rows:
        result[r["section_key"]] = {
            "data": json.loads(r["data"]),
            "updated_at": r["updated_at"],
        }
    return result


@router.put("/{lecture_num}/{section_key}")
def save_section(lecture_num: int, section_key: str, body: WorkbookSave):
    """Upsert a workbook section."""
    if lecture_num not in WORKBOOK_SECTIONS:
        raise HTTPException(status_code=404, detail=f"Lecture {lecture_num} not found")
    db = _get_db()
    now = datetime.now(timezone.utc).isoformat()
    db.execute(
        """INSERT INTO workbook_responses (lecture_num, section_key, data, updated_at)
           VALUES (?, ?, ?, ?)
           ON CONFLICT(lecture_num, section_key) DO UPDATE SET data = excluded.data, updated_at = excluded.updated_at""",
        (lecture_num, section_key, json.dumps(body.data), now),
    )
    db.commit()
    db.close()
    return {"status": "saved"}


@router.delete("/{lecture_num}/{section_key}")
def delete_section(lecture_num: int, section_key: str):
    """Clear a workbook section."""
    db = _get_db()
    db.execute(
        "DELETE FROM workbook_responses WHERE lecture_num = ? AND section_key = ?",
        (lecture_num, section_key),
    )
    db.commit()
    db.close()
    return {"status": "deleted"}

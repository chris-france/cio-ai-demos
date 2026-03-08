"""Demo API routes."""

from fastapi import APIRouter
from demos import FOUNDATION_DEMOS, ADVANCED_DEMOS, enrich_demos

router = APIRouter(prefix="/api")


@router.get("/demos")
def get_demos():
    return {
        "foundation": {
            "title": "Foundation Course",
            "subtitle": "Lectures 1-7",
            "description": (
                "All demos use Claude Code. Lecture 2 introduces Ollama for local model comparison. "
                "Pure terminal + CC."
            ),
            "demos": enrich_demos(FOUNDATION_DEMOS),
        },
        "advanced": {
            "title": "Advanced Course",
            "subtitle": "Lectures 7-12",
            "description": (
                "Advanced demos add local models (Ollama), UI-based tools, "
                "and self-hosted infrastructure."
            ),
            "demos": enrich_demos(ADVANCED_DEMOS),
        },
    }

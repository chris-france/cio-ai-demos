"""Demo API routes."""

from fastapi import APIRouter
from demos import (
    FOUNDATION_DEMOS, ADVANCED_DEMOS, SERVICE_MGMT_DEMOS,
    enrich_demos,
)

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
            "subtitle": "Lectures 8-15",
            "description": (
                "Strategy, communication, and execution: from mission alignment "
                "to vendor risk management."
            ),
            "demos": enrich_demos(ADVANCED_DEMOS),
        },
        "service_mgmt": {
            "title": "AI-Powered IT Service Management",
            "subtitle": "8 Lectures",
            "description": (
                "Transform your help desk from cost center to AI-powered resolution engine. "
                "Ticket classification, auto-resolution, SLA prediction, and transition planning."
            ),
            "demos": enrich_demos(SERVICE_MGMT_DEMOS),
        },
    }

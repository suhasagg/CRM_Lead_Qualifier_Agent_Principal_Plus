from enum import Enum
from pydantic import BaseModel, Field
from typing import Any
class Decision(str, Enum): QUALIFIED="QUALIFIED"; REVIEW="REVIEW"; DISQUALIFIED="DISQUALIFIED"
class Lead(BaseModel):
    lead_id: str; name: str; email: str; company: str; domain: str | None=None
    title: str | None=None; employee_count: int | None=None; country: str | None=None
    annual_revenue_usd: float | None=None; source: str | None=None; notes: str | None=None
class ToolTrace(BaseModel):
    tool: str; input: dict[str, Any]; output: dict[str, Any]; latency_ms: float
class QualificationResult(BaseModel):
    lead_id: str; score: int=Field(ge=0,le=100); decision: Decision; rationale: list[str]
    recommended_action: str; tool_trace: list[ToolTrace]=[]; model_used: str | None=None

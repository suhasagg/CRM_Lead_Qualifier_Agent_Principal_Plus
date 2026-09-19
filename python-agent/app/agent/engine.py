import time
from app.core.config import settings
from app.domain.models import Lead, QualificationResult, Decision, ToolTrace
from app.tools.domain_lookup import domain_lookup
from app.tools.crm_history import crm_history
from app.tools.scoring import score_lead

class LeadQualificationAgent:
    """Bounded Think→Act→Observe orchestrator. Tool execution is deterministic/auditable; LLM narration is optional."""
    async def qualify(self, lead: Lead) -> QualificationResult:
        traces=[]
        domain=lead.domain or lead.email.split("@")[-1]
        t=time.perf_counter(); enrich=await domain_lookup(domain)
        traces.append(ToolTrace(tool="domain_lookup",input={"domain":domain},output=enrich,latency_ms=(time.perf_counter()-t)*1000))
        t=time.perf_counter(); history=await crm_history(lead.lead_id)
        traces.append(ToolTrace(tool="crm_history",input={"lead_id":lead.lead_id},output=history,latency_ms=(time.perf_counter()-t)*1000))
        t=time.perf_counter(); scored=score_lead(lead.model_dump(),enrich,history)
        traces.append(ToolTrace(tool="lead_scoring",input={"lead_id":lead.lead_id},output=scored,latency_ms=(time.perf_counter()-t)*1000))
        s=scored["score"]
        if s>=settings.qualification_threshold: decision=Decision.QUALIFIED; action="Route to account executive and create priority follow-up task"
        elif s>=settings.review_threshold: decision=Decision.REVIEW; action="Queue for SDR human review and request missing firmographic data"
        else: decision=Decision.DISQUALIFIED; action="Place in nurture flow; do not create sales opportunity"
        return QualificationResult(lead_id=lead.lead_id,score=s,decision=decision,rationale=scored["reasons"],recommended_action=action,tool_trace=traces,model_used="deterministic-policy-engine")

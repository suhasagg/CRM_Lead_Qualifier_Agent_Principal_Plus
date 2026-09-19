import httpx
from app.core.config import settings
async def crm_history(lead_id: str) -> dict:
    try:
        async with httpx.AsyncClient(timeout=2.0) as c:
            r=await c.get(f"{settings.crm_base_url}/api/crm/leads/{lead_id}/history")
            if r.status_code==200: return r.json()
    except Exception: pass
    return {"leadId":lead_id,"previousOpportunities":0,"wonDeals":0,"lastContactDays":999,"doNotContact":False,"source":"fallback"}

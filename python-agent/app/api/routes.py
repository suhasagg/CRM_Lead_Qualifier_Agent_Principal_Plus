from fastapi import APIRouter, HTTPException
from app.domain.models import Lead, QualificationResult
from app.agent.engine import LeadQualificationAgent
router=APIRouter(); agent=LeadQualificationAgent()
@router.post('/qualify',response_model=QualificationResult)
async def qualify(lead:Lead):
    try: return await agent.qualify(lead)
    except Exception as e: raise HTTPException(500,detail="qualification failed") from e
@router.get('/health')
async def health(): return {"status":"ok"}

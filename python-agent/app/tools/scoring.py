def score_lead(lead: dict, enrichment: dict, history: dict) -> dict:
    score=0; reasons=[]
    employees=lead.get("employee_count") or enrichment.get("estimated_employees") or 0
    revenue=lead.get("annual_revenue_usd") or 0
    title=(lead.get("title") or "").lower()
    if employees>=1000: score+=25; reasons.append("enterprise employee scale")
    elif employees>=200: score+=18; reasons.append("mid-market employee scale")
    elif employees>=50: score+=10
    if revenue>=100_000_000: score+=20; reasons.append("high reported revenue")
    elif revenue>=10_000_000: score+=12
    if any(k in title for k in ["chief","cto","cio","vp","vice president","head","director"]): score+=20; reasons.append("senior buying-role signal")
    if history.get("wonDeals",0)>0: score+=20; reasons.append("prior won business")
    elif history.get("previousOpportunities",0)>0: score+=10; reasons.append("prior CRM opportunity")
    if history.get("lastContactDays",999)<30: score+=10; reasons.append("recent engagement")
    if enrichment.get("valid"): score+=5
    if history.get("doNotContact"): score=0; reasons.append("do-not-contact policy override")
    return {"score":min(score,100),"reasons":reasons}

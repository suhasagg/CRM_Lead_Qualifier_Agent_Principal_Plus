from app.tools.scoring import score_lead
def test_dnc_override():
    r=score_lead({"title":"CTO","employee_count":5000,"annual_revenue_usd":1e9},{"valid":True},{"wonDeals":3,"doNotContact":True})
    assert r["score"]==0
def test_enterprise_scores_high():
    r=score_lead({"title":"CTO","employee_count":5000,"annual_revenue_usd":1e9},{"valid":True},{"wonDeals":1,"lastContactDays":5,"doNotContact":False})
    assert r["score"]>=70

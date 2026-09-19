#!/usr/bin/env bash
curl -s http://localhost:8000/api/v1/qualify -H 'content-type: application/json' -d '{"lead_id":"L-1001","name":"Asha Rao","email":"asha@acmecloud.com","company":"Acme Cloud","domain":"acmecloud.com","title":"VP Engineering","employee_count":1800,"annual_revenue_usd":250000000,"country":"IN","source":"conference"}' | python -m json.tool

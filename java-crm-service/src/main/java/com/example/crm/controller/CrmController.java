package com.example.crm.controller;
import com.example.crm.model.LeadHistory; import com.example.crm.service.CrmHistoryService; import org.springframework.web.bind.annotation.*;
@RestController @RequestMapping("/api/crm/leads") public class CrmController { private final CrmHistoryService service; public CrmController(CrmHistoryService s){service=s;} @GetMapping("/{id}/history") public LeadHistory history(@PathVariable String id){return service.history(id);} }

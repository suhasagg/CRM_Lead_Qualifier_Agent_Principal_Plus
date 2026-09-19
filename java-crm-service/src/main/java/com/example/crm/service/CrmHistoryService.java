package com.example.crm.service;
import com.example.crm.model.LeadHistory; import org.springframework.stereotype.Service;
@Service public class CrmHistoryService {
 public LeadHistory history(String id){ int h=Math.abs(id.hashCode()); return new LeadHistory(id,h%4,h%3,(h%120)+1,false,"demo-crm"); }
}

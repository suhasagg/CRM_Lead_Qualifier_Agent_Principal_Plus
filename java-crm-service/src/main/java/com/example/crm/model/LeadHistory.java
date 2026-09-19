package com.example.crm.model;
public record LeadHistory(String leadId,int previousOpportunities,int wonDeals,int lastContactDays,boolean doNotContact,String source) {}

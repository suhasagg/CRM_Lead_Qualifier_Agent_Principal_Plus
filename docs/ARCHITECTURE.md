# Architecture Deep Dive

The README is the canonical principal-level architecture document. This companion captures implementation evolution.

## Phase 1 — modular monolith + CRM adapter
FastAPI performs orchestration and scoring; Spring Boot abstracts CRM. Optimize developer velocity and establish contracts.

## Phase 2 — durable workflow
Add Postgres workflow state, event ingestion, outbox, Redis evidence cache and OpenTelemetry. Make qualification resumable.

## Phase 3 — governed LLM planner
Introduce a model gateway and schema-constrained planner. Tool registry enforces capability permissions, budgets, timeouts and data policy.

## Phase 4 — platformization
Multi-tenant control plane, policy service, prompt/model registry, offline/online evaluation, reviewer UI, replay tooling and regional deployment.

## Control plane vs data plane
Control plane stores tenant configuration, tool permissions, prompt/policy versions, rollout rules and quotas. Data plane executes lead workflows and must continue safely using cached/versioned control state during transient control-plane failures.

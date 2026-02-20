# AI Tutor Platform (FastAPI + React)

A strong **starter implementation** for an AI tutoring platform with multilingual support, adaptive learning, voice accessibility, analytics, and gamification.

> Status: **Not fully production-complete yet.** Core architecture is in place, but you should complete the launch checklist below before going live at scale.

## Included capabilities

1. **Multi-language NLP**: Language detection and translation workflow for regional languages (`/chat/doubt`).
2. **Adaptive pathways**: Difficulty adapts using student performance (`/learning/progress`).
3. **Voice interaction**: STT + TTS interface (`/voice/interact`, simulation-ready for cloud speech providers).
4. **Personalized recommendations**: Content suggestions derived from learner history (`/learning/recommendations`).
5. **Gamification**: Points, levels, and achievement badges updated on each submission.
6. **Real-time doubt resolution**: AI chatbot endpoint with localization support.
7. **Analytics dashboard APIs**: Parent/teacher/student overview endpoint (`/analytics/overview/{student_id}`).
8. **Secure accounts**: JWT authentication, role-aware access controls.
9. **Scalability baseline**: Dockerized services and Kubernetes autoscaling starter.

## Project structure

- `backend/`: FastAPI service with auth, adaptive learning, chatbot, analytics, and recommendation engines.
- `frontend/`: React UI with modern, age-inclusive, multilingual experience controls.
- `infra/k8s/`: Kubernetes deployment + HPA baseline for cloud rollout.
- `docker-compose.yml`: Local multi-service stack.

## Quick start

```bash
# backend
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

# frontend (new terminal)
cd frontend
npm install
npm run dev
```

## Launch checklist (recommended next steps)

### 1) Replace development defaults (mandatory)
- Move `SECRET_KEY` and other secrets to environment variables or a secret manager.
- Replace SQLite with managed PostgreSQL + migrations.
- Add Redis for caching/session/rate-limit counters.

### 2) Upgrade AI layer
- Replace rule-based chatbot responses with an LLM service and moderation guardrails.
- Add prompt templates per age group (early learner, school, higher-ed, adult).
- Add multilingual evaluation tests for quality and safety.

### 3) Production security & compliance
- Add refresh tokens, rotation, token revocation strategy.
- Add RBAC policy checks for all protected routes.
- Add audit logs, PII protections, and data retention policies.
- Add HTTPS, WAF, and API gateway throttling.

### 4) Reliability & observability
- Add structured logging, tracing, metrics dashboards, and alerting.
- Add background workers for recommendation refresh and analytics aggregation.
- Configure autoscaling for API and workers based on CPU + queue latency.

### 5) Frontend UX hardening
- Connect all UI controls to real backend APIs.
- Add onboarding wizard, per-age lesson themes, and accessibility profiles.
- Add E2E tests (Playwright/Cypress) for language, voice, and adaptive flow.

### 6) Deploy to cloud
- Build and push images to your container registry.
- Deploy using managed Kubernetes (EKS/GKE/AKS) or a PaaS equivalent.
- Put API behind a load balancer, set domain + TLS, and configure CDN for frontend.


## Free launch path (no-cost assignment deployment)

If you want the fastest **free-of-cost** launch path, follow: `FREE_DEPLOYMENT.md`.

## Testing

```bash
cd backend
pytest
python -m compileall app
```

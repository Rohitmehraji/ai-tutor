# Free-Cost Deployment (Minimum Assignment-Completion Path)

If your goal is **"submit assignment + make it live at zero cost"**, use this exact path:

- **Backend API**: Render (free web service)
- **Database**: Neon Postgres (free tier)
- **Frontend**: Vercel (free tier)

This is the lowest-effort practical route for this repo.

---

## 0) What "free" means

- No upfront payment.
- Services can sleep/spin down on inactivity.
- Performance is enough for demo/assignment, not for heavy production traffic.

---

## 1) Prepare backend for cloud (10 minutes)

### 1.1 Set database URL from environment
Current backend uses local SQLite by default. For cloud, set `DATABASE_URL`.

Use this environment variable format (Neon gives you full URL):

```bash
postgresql+psycopg://USER:PASSWORD@HOST/DBNAME?sslmode=require
```

### 1.2 Install Postgres driver
In `backend/requirements.txt`, ensure this exists:

```txt
psycopg[binary]
```

(If missing, add it before deployment.)

### 1.3 Update database config
Use environment variable fallback logic:

```python
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ai_tutor.db")
```

And only apply `check_same_thread=False` for SQLite.

---

## 2) Create free database (Neon)

1. Sign up at Neon (free).
2. Create project + database.
3. Copy connection string.
4. Keep it safe; you will paste it in Render env vars.

---

## 3) Deploy backend free on Render

1. Push your repo to GitHub.
2. In Render: **New Web Service** → connect GitHub repo.
3. Root directory: `backend`
4. Build command:

```bash
pip install -r requirements.txt
```

5. Start command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

6. Add environment variables in Render:

- `DATABASE_URL` = your Neon URL
- `AI_TUTOR_SECRET_KEY` = any long random string
- `AI_TUTOR_JWT_ALGORITHM` = `HS256`
- `AI_TUTOR_ACCESS_TOKEN_MINUTES` = `1440`

7. Deploy and open:

```text
https://your-backend-name.onrender.com/docs
```

If docs load, backend is live.

---

## 4) Deploy frontend free on Vercel

1. In Vercel: import same GitHub repo.
2. Root directory: `frontend`
3. Framework preset: Vite (auto-detected usually).
4. Build command:

```bash
npm run build
```

5. Output directory:

```bash
dist
```

6. Add env var (if using API URL in frontend code):

- `VITE_API_BASE_URL=https://your-backend-name.onrender.com`

7. Deploy. You get:

```text
https://your-frontend-name.vercel.app
```

---

## 5) Minimum demo checklist for assignment submission

- [ ] Register user works
- [ ] Login returns JWT
- [ ] Submit progress endpoint works
- [ ] Chat/doubt endpoint works
- [ ] Analytics endpoint returns data
- [ ] Frontend opens and shows modern UI
- [ ] Add 2 screenshots + deployed links in your report

---

## 6) Known free-tier limits (so you are not surprised)

- Render free service may sleep when idle (first request can be slow).
- Free DB/storage/compute quotas are limited.
- Not suitable for "millions of users" scale.

For assignment/demo: this is completely fine.

---

## 7) One-line answer to "is it complete?"

For **assignment-level live deployment**: yes, after steps above.

For **serious production at scale**: no, you still need paid infra + hardening.

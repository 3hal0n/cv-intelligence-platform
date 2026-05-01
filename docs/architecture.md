# System Architecture: AI CV Matcher

## 1. High-Level Stack (Zero-Cost MVP)
- **Frontend:** Next.js (App Router), Tailwind CSS, Framer Motion (Deployed on Vercel)
- **Backend:** FastAPI, Python 3.10+ (Deployed on Render - Free Tier)
- **Database & Auth:** Supabase (PostgreSQL, Free Tier)
- **AI Engine:** Azure OpenAI (`gpt-4o-mini`) using Student Credits

## 2. Core Components

### A. The Client (Next.js)
- Handles UI, drag-and-drop file uploads.
- Manages state for "Blind Screening" (DEI toggle).
- Renders PDF alongside extracted insights using `react-pdf-highlighter`.

### B. The API (FastAPI)
- **Endpoint:** `/api/v1/analyze`
- Parses PDF locally using `PyMuPDF` (Zero API cost).
- Runs BS Detector (keyword density analysis) locally.
- Sends a single, optimized prompt to Azure OpenAI.
- Uses FastAPI `BackgroundTasks` for basic asynchronous processing to prevent Render timeouts.

### C. Data Layer (Supabase)
- Stores job descriptions and parsed CV metadata.
- (Future) `pgvector` extension for semantic search across candidate pools.

## 3. Cost Optimization Strategy
- **No PDF Uploads to LLM:** Extract text locally, chunk, and clean before sending.
- **One-Shot JSON Prompt:** Get summary, skills, and interview questions in a single API call.
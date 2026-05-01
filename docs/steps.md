# Step-by-Step Development Guide

### Step 1: Repository & Environment Setup
- Initialize Git repository.
- Create `/frontend` (Next.js) and `/backend` (FastAPI) directories.
- Set up `.env` files for Supabase and Azure OpenAI keys.

### Step 2: Backend Core (FastAPI)
- Set up virtual environment (`venv`).
- Install `fastapi`, `uvicorn`, `pymupdf`, `openai`, `supabase`.
- Create `/upload` endpoint.
- Write PDF text extraction utility.

### Step 3: AI Integration & Prompting
- Write the master JSON prompt requesting: match score, skills, missing skills, summaries (regular & redacted), and interview questions.
- Implement Azure OpenAI API call.
- Add Python logic for the BS Detector (keyword density > 10%).

### Step 4: Frontend Core (Next.js)
- Initialize Next.js with Tailwind and Framer Motion for smooth UI transitions.
- Build File Upload component (support single & small bulk).
- Create Dashboard layout to display results.

### Step 5: Feature Implementation
- Add state toggle for DEI Blind Screening.
- Render Targeted Interview Questions cards.
- *Advanced:* Integrate `react-pdf-highlighter` and map AI text matches to PDF coordinates.

### Step 6: Deployment
- Deploy Frontend to Vercel.
- Deploy Backend to Render (configure start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`).
- Link Supabase database.
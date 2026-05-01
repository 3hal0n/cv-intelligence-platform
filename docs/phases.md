# Project Phases

## Phase 1: Core Engine & Pipeline
*Goal: Establish the basic end-to-end flow.*
1. Build Next.js upload UI.
2. Set up FastAPI endpoint to receive PDFs.
3. Integrate `PyMuPDF` to extract text.
4. Design the "One-Shot" JSON prompt for Azure OpenAI.
5. Save the output to Supabase.

## Phase 2: Feature Integration (The Differentiators)
*Goal: Implement the core selling points.*
1. **BS Detector:** Add Python logic to calculate keyword density before AI processing.
2. **Targeted Interview Generator:** Map the LLM output array to UI cards.
3. **DEI Blind Screening:** Implement frontend toggle to switch between `smart_summary` and `dei_redacted_summary`.

## Phase 3: The "Wow" Factor
*Goal: Build the interactive PDF viewer.*
1. Integrate `react-pdf-highlighter`.
2. Map the exact quotes returned by the LLM to text boundaries in the rendered PDF.
3. Implement click-to-highlight interaction in the UI.
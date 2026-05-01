# main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from utils.pdf_extractor import extract_clean_text

app = FastAPI(title="AI CV Matcher API")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/upload")
async def upload_cv(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a PDF.")
    
    try:
        file_bytes = await file.read()
        
        # Extract text locally (Zero Cost)
        cv_text = extract_clean_text(file_bytes)
        
        # TODO: Add BS Detector logic and Azure OpenAI call here
        
        return {
            "status": "success",
            "filename": file.filename,
            "character_count": len(cv_text),
            "text_preview": cv_text[:250] + "..." # Preview for testing
        }
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error during processing.")
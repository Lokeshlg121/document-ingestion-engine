from fastapi import FastAPI,File, HTTPException,UploadFile
from document_ingestion.extraction.pdf.text import extract_text

app = FastAPI(title="Document Ingestion Engine")

@app.get("/health")
def health_check():
    return {"status": "Healthy"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a PDf file."
        )
    try:
        contents = await file.read()

        if not contents:
            raise HTTPException(
                status_code=400,
                detail= "The uploaded file is empty"
            )
        result = extract_text(contents)
        return result
    except HTTPException:
        raise 
    except Exception as exc:
        raise HTTPException(
            status_code=400,
            detail="Could not read the uploaded PDF."
        ) from exc
    finally:
        await file.close()
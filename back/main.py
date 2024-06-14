from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import uvicorn
from typing import List

app = FastAPI()

@app.post("/summary")
async def summarize_document(files: List[UploadFile] = File(...)):
    summaries = []
    for file in files:
        content = await file.read()
        print(f"Received file: {file.filename}, size: {len(content)} bytes")
        summaries.append({"filename": file.filename, "summary": content[:100]})

    #### Add llms call here ####
    summary = str(summaries)
    return JSONResponse(content={"summary": summary}, status_code=200)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

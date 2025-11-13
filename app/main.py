from fastapi import FastAPI, UploadFile, File
from routes import tasks
from config import upload_file_to_s3
import os

app = FastAPI(title="TaskBoard DevOps", version="1.0.0")

app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def home():
    return {"message": "🚀 TaskBoard API corriendo correctamente en EC2
                           Hecho por Thiago Lovey"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    local_path = f"app/static/{file.filename}"
    with open(local_path, "wb") as f:
        f.write(content)

    # Subir a S3
    upload_file_to_s3(local_path, file.filename)

    os.remove(local_path)
    return {"status": "success", "filename": file.filename}

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import uvicorn
import cv2
import numpy as np
import os
from PIL import Image

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/colorize/")
async def colorize_image(file: UploadFile = File(...)):
    # Save uploaded image
    contents = await file.read()
    input_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(input_path, "wb") as f:
        f.write(contents)

    # Load image using OpenCV
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        return {"error": "Failed to read image"}

    # Colorize (basic grayscale to BGR — replace with deep model inference if needed)
    img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    # Save result
    output_path = os.path.join(UPLOAD_DIR, "colorized_" + file.filename)
    cv2.imwrite(output_path, img_color)

    return FileResponse(output_path, media_type="image/jpeg")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

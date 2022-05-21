from PIL import Image, ImageFilter
from fastapi import FastAPI, Depends, File, UploadFile
from starlette.responses import StreamingResponse
from io import BytesIO
import uvicorn

app = FastAPI()


@app.get("/")
async def hello():
    return {"result": "Its working YES!"}


@app.post("/CONTOUR")
async def image_filter(img: UploadFile = File(...)):
    original_image = Image.open(img.file)
    original_image = original_image.filter(ImageFilter.CONTOUR)
    #CONTOUR, EMBOSS, FIND_EDGES
    filtered_image = BytesIO()
    original_image.save(filtered_image, "JPEG")
    filtered_image.seek(0)

    return StreamingResponse(filtered_image, media_type="image/jpg")


@app.post("/EMBOSS")
async def image_filter(img: UploadFile = File(...)):
    original_image = Image.open(img.file)
    original_image = original_image.filter(ImageFilter.EMBOSS)
    #CONTOUR, EMBOSS, FIND_EDGES
    filtered_image = BytesIO()
    original_image.save(filtered_image, "JPEG")
    filtered_image.seek(0)

    return StreamingResponse(filtered_image, media_type="image/jpg")

@app.post("/EDGES")
async def image_filter(img: UploadFile = File(...)):
    original_image = Image.open(img.file)
    original_image = original_image.filter(ImageFilter.FIND_EDGES)
    #CONTOUR, EMBOSS, FIND_EDGES
    filtered_image = BytesIO()
    original_image.save(filtered_image, "JPEG")
    filtered_image.seek(0)

    return StreamingResponse(filtered_image, media_type="image/jpg")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")

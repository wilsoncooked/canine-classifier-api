from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from snoop_dog.registry import load_dogmodel
from snoop_dog.main import predict_breeds

app = FastAPI()

# Allow all requests (optional, good for development purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.state.model = None

@app.get("/")
def index():
    return {"status": "ok"}

@app.get("/start")
def start():
    if not app.state.model:
        app.state.model = load_dogmodel()
    return {"status": "started"}

@app.post('/upload_image')
async def receive_image(img: UploadFile=File(...)):
    model = app.state.model
    image = img.file
    result = predict_breeds(model, image)
    ### Encoding and responding with the image
    return result

from fastapi import FastAPI, APIRouter

app = FastAPI()

@app.get("/")
async def index():
    return {"Hello": }

@app.get("/registration")
async def registration():
    return {'rqg':'dd'}

reg_router = APIRouter(prefix="/registration", tags=["registration"])

@reg_router.post("/success")
async def pub():
    return {"":'',"":' '}
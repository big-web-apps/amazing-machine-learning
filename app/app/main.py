from fastapi import FastAPI
from .predict import predict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root(rooms: int, square: float, floor: int, price: int):
    return {'coefficient': predict([rooms, square, floor, price])}

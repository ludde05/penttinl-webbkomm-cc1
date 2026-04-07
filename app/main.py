from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

hot_rooms = [
    {"roomNumber": 1, "type": "single", "price": 100},
    {"roomNumber": 2, "type": "family", "price": 400},
    {"roomNumber": 3, "type": "double", "price": 200},
]

@app.get("/")
def read_root():
    return { "msg": "Hotel booking", "v": "0.1" }


@app.get("/rooms")
def rooms():
    return {"msg": "Available rooms", "rooms": hot_rooms}

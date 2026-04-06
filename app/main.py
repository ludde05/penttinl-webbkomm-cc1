from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return { "msg": "Morjesta!", "v": "0.1" }


@app.get("/items/{id}")
def read_item(item_id: int, q: str = None):
    return {"id": id, "q": q}

@app.get("/hello")
def hello():
    return { "msg": "Moro Ludde"}

    
@app.get("/api/ip")
def ip(request: Request):
    return { "ip": request.client.host }

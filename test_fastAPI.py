from fastapi import FastAPI
from pydantic import BaseModel

class MyItem(BaseModel):
    name:str
    price:float
    ready:int = 0

app = FastAPI()

@app.get("/")
async def home():
    return "Đây là home"

@app.post("/submit")
async def submit(item: MyItem):
    print(item)
    print(item.name)
    # return "Save thành công"
    return item.name
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app=FastAPI()

class Item(BaseModel):
    id:int
    name:str
    description:str
    category:str
    owner:str

items:List[Item]=[]

@app.get("/")
def read_root():
    return{"message":"Welcome to Ishwar's Project"}

@app.post("/items")
def add_item(item:Item):
    items.append(item)
    return item

@app.get("/items")
def get_items():
    return items

@app.get("/items/{item_id}")
def get_item(item_id:int):
    for item in items:
        if item.id==item_id:
            return item
    return{"error":"Item not found"}

@app.put("/items/{item_id}")
def update_item(item_id:int,update_item:Item):
    for index,item in enumerate(items):
        if item.id==item_id:
            items[index]=update_item
            return update_item
    return {"error":"Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    for index,item in enumerate(items):
        if item.id==item_id:
            deleted=items.pop(index)
            return deleted
    return {"error":"Item not found"}


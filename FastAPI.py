from ast import keyword
from http.client import FOUND
from fastapi import FastAPI, Path, Query, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str]=None

class UpdateItem(BaseModel):
    name: Optional[str]=None
    price: Optional[float]=None
    brand: Optional[str]=None

@app.get("/")
def home():
    return {"Data": "Test"}             #dictonary is displayed as JSON (object of JavaScript)

@app.get("/about")
def about():
    return {"Data": "About"}

inventory = {

    1: {                                #1 is the inventory id
        "name" : "Milk",
        "price" : 25,
        "brand": "Amul",
    }
}

@app.get("/get-item/{item_id}")         #"..." enclosed is the end point. Should be same as the local URL for function below to execute
def get_item(item_id: int = Path(None, description = "The ID of the item you would like to view", gt=0)):            
                                        #int is specified so that API automatically sends an error if the input is not an integer
    return inventory[item_id]           

#Query Paramter - the type is "?variable= ..." 
@app.get("/get-by-name/{item_id}")
def get_by_name(name: Optional[str], item_id: int):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
        return {"Data": "Not found"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error!... Item already exists"}
    inventory[item_id] = {"name": item.name, "price": item.price, "brand": item.brand}
    return inventory[item_id]

#Update an item
@app.put("/update-item")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error!... Item does not exist"} 
    if item.name !=None:
        inventory[item_id]["name"] = item.name
    if item.price !=None:
        inventory[item_id]["price"] = item.price
    if item.brand !=None:
        inventory[item_id]["brand"] = item.brand
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int):              #def delete_item(item_id: int= Query(..., description="The ID of the item to be deleted"))
    if item_id not in inventory:
        return {"Error!... ID does not exist"}
    del inventory[item_id]
    return {"Successfully Deleted"}


# Status Codes and Exceptions
# raise HTTPException(status_code=404, detail= "Item does not exist") - syntax
# Exceptions raised as basic python exceptions just with a different keyword
# Status Codes are what is returned by the API automatically but can be user defined to print error messages
# Example- 200: Successfully FOUND


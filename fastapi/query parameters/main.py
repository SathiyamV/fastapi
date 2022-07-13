from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def Hello_Universe():
    return{"Hello":"Universe !"}

@app.get("/component/{component_id}")
async def get_component(component_id:int):
    return{"component_id":component_id}
@app.get("/component")
async def read_component(number:int,text: str):
    return{"number":number,"text":text}

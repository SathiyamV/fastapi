

from typing import Optional
from fastapi import FastAPI

from pydantic import BaseModel

class Package(BaseModel):
    name: str
    number: str
    description: Optional[str] = None

app = FastAPI()

@app.get('/')
async def hello_world():
    return {'Hello' : 'World'}

@app.post("/package/")
async def make_package(Package):
    return Package
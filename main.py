from fastapi import FastApi
from fastaapi.cors import CorsMiddleware


app = FastApi(__dirname__)
@app.get('/')
async def sayhello():
  return {'greeting': 'hallo'}




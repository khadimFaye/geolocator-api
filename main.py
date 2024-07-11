from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

#inizializza fastapi 
app = FastAPI()
#aggiungui corsmiddle ware per gestire meglio i blocchi dovuti ai cors durante le requets http
app.add_middleware(
  CORSMiddleware,
    
    allow_credentials=True,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
  )
#test the firs route
@app.get('/')
async def sayhello():
  return {'greeting': 'hallo'}


if __name__=='__main__':
  uvicorn.run(app)




from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils import ip_calc

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello", "World"}


@app.get('/ipcalc/{ip}')
def do_ip_calc(ip: str, mask: str):
    result = ip_calc(ip, mask)
    return result

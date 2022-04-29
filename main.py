'''
IP calculator to convert decimal to binary
'''
from fastapi import FastAPI
from utils import ip_to_binary, number_to_binary

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello")
def read_root():
    return {"Hello": "World"}

@app.post('/to_binary')
def to_binary(number):
    result = number_to_binary(int(number))
    return result

@app.post('/ip_to_binary')
def ip_binary(ip):
    result = ip_to_binary(ip)
    return result

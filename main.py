'''
IP calculator to convert decimal to binary
'''
from fastapi import FastAPI
from utils import ip_calc

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/ipcalc')
def do_ip_calc(ip: str, mask: str):
    result = ip_calc(ip, mask)
    return result

# @app.post('/ip_to_binary')
# def ip_binary(ip):
#     result = ip_to_binary(ip)
#     return result

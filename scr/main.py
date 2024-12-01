from typing import Union

from fastapi import FastAPI
import redis

app = FastAPI()

r =redis.Redis(host="redis",port=6379)
@app.get("/")
def read_root():
    return {"Hello": "Arti, i am kewal, i love you more"}


@app.get("/hits")
def read_root():
    r.incr('hits')
    return {"no. of hits":r.get(hits)}
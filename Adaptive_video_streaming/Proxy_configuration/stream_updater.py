import webbrowser
from fastapi import FastAPI
import threading 
import time
import json
import requests
import pandas as pd
import uvicorn

app = FastAPI()
i = 0

def open_browser(url= str):
    webbrowser.open(url=url)

@app.get('/update')
async def update_stream(data: dict):
    global i
    print(f"New stream endpoint is: {data}")
    for item in data:
        if i == 0:
            open_browser(data[item])


    


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
    print("server running")
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from typing import Optional
import json
import os
import math

app = FastAPI()

@app.get("/data")
async def read_data(page: Optional[int] = 1, page_size: Optional[int] = 20):
    try:
        with open('my_apis.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Data not found")
    
    start = (page - 1) * page_size
    end = start + page_size
    return data[start:end]

@app.get("/total_pages")
async def total_pages(page_size: Optional[int] = 20):
    try:
        with open('my_apis.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Data not found")
    
    total_pages = math.ceil(len(data) / page_size)
    return {"total_pages": total_pages}

@app.get("/", response_class=HTMLResponse)
async def read_home():
    try:
        with open('index.html', 'r') as f:
            html_content = f.read()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="HTML file not found")
    return html_content

from fastapi import FastAPI, Request
from pydantic import BaseModel
import base64
import json
import os
import aiofiles
from typing import List, Any
import cv2
import numpy as np


def handle_objs(targets):
    result = {
        "people": [],
        "car": [],
        "animal": [],
    }
    for target in targets:
        result[target.type].append(target)
    return result

class Target(BaseModel):
    index: int
    width: int
    height: int
    left: int
    top: int
    type: str

class Item(BaseModel):
    task_no: Any
    keyframe: Any
    targets: Any
    date: Any

class Response(BaseModel):
    status: str

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    jpg_original = base64.b64decode(item.keyframe.encode('utf8'))
    jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
    keyframe = cv2.imdecode(jpg_as_np, flags=1)
    if not os.path.exists(f'./{item.task_no}'):
        os.mkdir(f'./{item.task_no}')
    cv2.imwrite(f"./{item.task_no}/keyframe.jpg", keyframe) 
    print(f"task_no: {item.task_no} date: {item.date}")
    # handle_result = handle_objs(item.targets)
    # print(f"people: {len(handle_result['people'])}, car: {len(handle_result['car'])}, animal: {len(handle_result['animal'])}")
    response = Response(status='200')
    return response

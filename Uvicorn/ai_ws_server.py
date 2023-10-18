import asyncio
import websockets
import json
import random


async def hello(websocket):
    task_no = str(random.randint(10000, 30000))
    #task_no = 10226
    print(await websocket.recv())
    msg = {
        "action": "AI_CONNECT",
        "data": {},
        "status": 0
    }
    await websocket.send(json.dumps(msg))

    # msg = {
    #     "action": "AI_TASK",
    #     "data": {
    #         "video_pull_url": "rtmp://172.17.0.1:1935/live/source",
    #         "video_push_url": f"rtmp://172.17.0.1:1935/live/{task_no}",
    #         "ai_type": ["car", "people", "animal"],
    #         "keyframe_push_url": "http://172.17.0.1:8899/items/",
    #         "task_no": task_no,
    #     }
    # }
    # print(f"rtmp://172.17.0.1:1935/live/{task_no}")
    # await websocket.send(json.dumps(msg))
    # resposne = await websocket.recv()
    # print(f">>> {resposne}")
    # await asyncio.sleep(60)


    msg = {
        "action": "AI_COMPLETE",
        "data": {
            "task_no": task_no,
        }
    }
    await websocket.send(json.dumps(msg))
    print("send msg")
    resposne = await websocket.recv()
    print(f">>> {resposne}")
    while True:
       resposne = await websocket.recv()
       print(f">>> {resposne}")     


async def main():
    async with websockets.serve(hello, "0.0.0.0", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())

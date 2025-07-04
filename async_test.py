import asyncio
import requests

async def runafter(secs):
	print("what")
	await asyncio.sleep(secs)
	print("the")
	await asyncio.sleep(secs * (2))
	print("actual")
	await asyncio.sleep(secs * (2 + 1))
	print("haha, gotcha")

async def tryupload(text,secs):
	await asyncio.sleep(1)
	print(f"sending: [{text}]")

secs_towait = input("enter seconds between prints: ")
what = input("what to upload: ")

asyncio.run(tryupload(what,float(secs_towait)*2))
asyncio.run(runafter(float(secs_towait)))

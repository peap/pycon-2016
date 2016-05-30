#!/usr/bin/env python3.5
import asyncio
import datetime

async def anything(i):  # <-- coroutine function
    print(i, datetime.datetime.now())
    await asyncio.sleep(i)

if __name__ == '__main__':
    loop  = asyncio.get_event_loop()
    loop.call_later(2, loop.stop)
    for i in range(1, 4):
        loop.create_task(anything(i)) # anything(i) <-- coroutine
    try:
        loop.run_forever()
        # loop.run_until_complete(loop.wait(tasks))
    finally:
        loop.close()

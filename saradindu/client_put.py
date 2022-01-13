# client_put.py
import asyncio
import random
import time
import struct
from aiocoap import *
async def main(p_dis):
        context = await Context.create_client_context()
        payload = struct.pack("f", p_dis)

        request = Message(code=PUT, payload=payload, uri="coap://localhost/proximity")

        response = await context.request(request).response
        output=struct.unpack("f",payload)
        print("Result ",response.code," ",output)
        #print('Result: %s\n%s'%(response.code,output))
        time.sleep(1)
'''
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main(p_dis))'''
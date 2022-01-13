import aiocoap.resource as resource
import aiocoap
import asyncio
import struct

class ProximityResource(resource.Resource):

    def __init__(self):
        super().__init__()
        self.state = "0"

    async def render_put(self, request):
        self.state = request.payload
        input=struct.unpack("f",self.state)
        print('Update Proximity distance: %s' % input)

        return aiocoap.Message(code=aiocoap.CHANGED, payload=self.state)


def main():
    # Resource tree creation
    root = resource.Site()
    root.add_resource(['proximity'], ProximityResource())

    asyncio.Task(aiocoap.Context.create_server_context(root, bind=('localhost', 5683)))

    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()

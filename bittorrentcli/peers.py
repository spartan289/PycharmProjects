import asyncio
class Peer():
    def __init__(self,host,port,file_queue):
        self.host=host
        self.port =port
        self.file_queue = file_queue

        self.peer_choking=True
        self.am_interested=False

    async def download(self,info_hash,peer_id):
        reader, writer = await asyncio.open_connection(
            self.host,self.port,
        )
        handshake = b''.join([
            chr(19).encode(),
            b'BitTorrent Protocol',
            (chr(0)*8).encode(),
            info_hash,
            peer_id
        ])

        writer.write(handshake)
        await writer.drain()


        peer_handshake = await reader.read(68)
        print(peer_handshake)
        self.validate(peer_handshake)

# peer = Peer()
# peer.host='194.159.69.65'
# peer.port=49821
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# loop.run_until_complete(peer.download(b'\x1e\x9b\xd3\xf1\xfdPb\xe1\x11\xb84\xd1\x8c\xbb&\xban.\x9d\x11',b'\x10\xcc\x913@7\x1a\xea`a=\n\x8c`\x0b\xc8h\xdd|\xab'))
# loop.close()
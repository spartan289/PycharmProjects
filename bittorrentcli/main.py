# # # This is a sample Python script.
# #
# # # Press Shift+F10 to execute it or replace it with your code.
# # # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import socket
# import struct
# from bcoding import bencode,bdecode
# import time
# import urllib
# import torrent_parser as tp
# import bencode as ben
# ##### in BIN folder
# # torrent_file = './torrents/Madhouse (Prince) - 08 - Eight.torrent'
# with open('B8E247869E0EA480336F41A9FDF63B4BF8FF7C50.torrent','rb') as file:
#     contents = bdecode(file)
# data = contents
# # See PyCharelp at https://www.jetbrains.com/help/pycharm/
# import requests
# from hashlib import sha1
# from urllib import parse
# # print(parse.quote(info_hash.hexdigest().encode('utf-8')))
# #
# # print(data['info'])
# #finding info hash
# info_to_buf = bencode(data['info'])
# info_hash = sha1(info_to_buf).digest()
#
# print(info_hash)
# #total_length
# total_size=0
# info = dict(data['info'])
# # print(type(info))
# # print(info['files'])
# for each_index in info['files']:
#     total_size += each_index['length']
# print(total_size)
#
#
#
# #peer_id
# def generate_peerid():
#     seed = str(time.time())
#     return sha1(seed.encode('utf-8')).digest()
# peer_id = generate_peerid()
# print(peer_id)
# param = {
#     'info_hash': info_hash,
#     'peer_id': peer_id,
#     'port': 24032,
#     'uploaded': 0,
#     'downloaded': 0,
#     'left': total_size,
#     'event': 'started'
# }
#
# print(param)
# print(data['announce'])
# print(data['announce-list'])
# import struct
# import socket
# connectionlist = []
# for i in data['announce-list']:
#     if i[0][0]=='h':
#         try:
#             print(i)
#             request = requests.get(i[0],params=param,timeout=5)
#             print(request)
#             # print(request.text)
#             p = ben.bdecode(request.text)
#             print(p)
#             offset=0
#             print(type(p['peers']))
#             x = p['peers'].encode()
#             print(len(p['peers']))
#             for i in range(len(p['peers'])//6):
#                 ip = struct.unpack_from('!i',x,offset)[0]
#                 ip_addr = socket.inet_ntoa(struct.pack("!i",ip))
#                 print(ip_addr)
#                 offset+=4
#                 port = struct.unpack_from('!H',x,offset)[0]
#                 print(port)
#                 offset+=2
#                 connectionlist.append((ip_addr,port))
#         except Exception as e:
#             print(e)
# def connecttopeer(connectionlist):
#     for i in connectionlist:
#         try:
#             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             s.connect(i)
#             s.send(b'hello')
#             print(s.recv(1024))
#         except Exception as e:
#             print(e)
# connecttopeer(connectionlist)


# print

from torrent import Torrent
import asyncio
from tracker import Tracker,Peer

async def download(torrent_file):
    torrent = Torrent(torrent_file)
    tracker=Tracker(torrent)

    peers = await tracker.get_peers()
    print(peers)
    print(len(peers))
    peers = [Peer(host,port,[]) for host,port in peers]
    for peer in peers:
        try:
            await peer.download(torrent.info_hash)
        except:
            print("Peer not Working")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.run_until_complete(download('EB0F6869ED9523857AF98CCFB0952CD6D636D56D.torrent'))

    loop.close()
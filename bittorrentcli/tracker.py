import asyncio
import ipaddress
import socket
import struct
from urllib import parse as urlparse

import aiohttp
import bencoder
import requests
from bcoding import bencode,bdecode

import torrent_parser
# import yarl

from torrent import Torrent
from utils import LOG, PEER_ID


class Tracker(object):
    def __init__(self, torrent : Torrent):
        self.torrent = torrent
        self.tracker_url = torrent.announce_url
        print()
        self.peers = []

    async def get_peers(self):
        peers_resp = self.request_peers()
        print(peers_resp)
        peers = self.parse_peers(peers_resp['peers'])
        return peers

    def request_peers(self):
        global peers
        print(self._get_request_params())

        for tracker_url in self.torrent.__getitem__('announce-list'):
            try:
                trackerurl = tracker_url[0]
                if(trackerurl[0]=='h'):
                    print(trackerurl)
                    resp =  requests.get(tracker_url[0], params=self._get_request_params(),timeout=5)
                    if (resp.status_code!=200):
                        continue
                    resp_data = resp.content
                    LOG.info('Tracker response: {}'.format(resp))
                    peers = None

                    try:
                        peers=bdecode(resp.content)
                    except AssertionError:
                        LOG.error('Failed to decode Tracker response: {}'.format(resp_data))
                        LOG.error('Tracker request URL: {}'.format(str(resp.url).split('&')))
                        raise RuntimeError('Failed to get Peers from Tracker')
            except Exception as e:
                print(e)
        return peers

    def _get_request_params(self):

        return {
            'info_hash': self.torrent.info_hash,
            'peer_id': PEER_ID,
            'compact': 1,
            'event': 'started',
            'port': 59696,
            'uploaded': 0,
            'downloaded': 0,
            'left': self.torrent.size
        }

    def parse_peers(self, peers : bytes):
        self_addr = socket.gethostbyname(socket.gethostname())
        LOG.info('Self addr is: {}'.format(self_addr))


        def handle_bytes(peers_data):
            peers = []
            for i in range(0, len(peers_data), 6):
                addr_bytes, port_bytes = (
                    peers_data[i:i + 4], peers_data[i + 4:i + 6]
                )
                ip_addr = str(ipaddress.IPv4Address(addr_bytes))
                if ip_addr == self_addr:
                    print('skipping', ip_addr)
                    continue
                port_bytes = struct.unpack('>H', port_bytes)[0]
                peers.append((ip_addr, port_bytes))
            return peers

        def handle_dict(peers):
            raise NotImplementedError

        handlers = {
            bytes: handle_bytes,
            dict: handle_dict
        }
        return handlers[type(peers)](peers)

class Peer():
    def __init__(self,host,port,file_queue):
        self.host=host
        self.port =port
        self.file_queue = file_queue

        self.peer_choking=True
        self.am_interested=False

    async def download(self,info_hash,):
        reader, writer = await asyncio.open_connection(
            self.host,self.port,
        )
        handshake = b''.join([
            chr(19).encode(),
            b'BitTorrent Protocol',
            (chr(0)*8).encode(),
            info_hash,
            PEER_ID
        ])
        print(handshake)
        writer.write(handshake)
        await writer.drain()


        peer_handshake = await reader.read(68)
        print(peer_handshake)
        self.validate(peer_handshake)
import copy
import hashlib
from pprint import pformat

from bcoding import bencode,bdecode

import torrent_parser as tp
class Torrent(object):
    def __init__(self, path : str):
        self.path = path
        self.info = self.read_torrent_file(path)


    def __getitem__(self, item):
        return self.info[item]

    def get_piece_hash(self, piece_idx):
        return self.info['info']['pieces'][piece_idx*20: (piece_idx*20) + 20]

    @property
    def announce_url(self) -> str:
        return self.info['announce']

    @property
    def info_hash(self):


        with open(self.path, 'rb') as file:
            contents = bdecode(file)
        data = contents

        info_to_buf = bencode(data['info'])
        info_hash = hashlib.sha1(info_to_buf).digest()
        return info_hash
    @property
    def size(self):
        info = self.info['info']
        if b'length' in info:
            return int(info['length'])
        else:
            return sum([int(f['length']) for f in info['files']])

    def read_torrent_file(self, path : str) -> dict:

        with open(path,'rb') as file:
           content =bdecode(file)
        return content

    def __str__(self):
        # info = copy.deepcopy(self.info)
        # del info[b'info'][b'pieces']
        return pformat(self.info)

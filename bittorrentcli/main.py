# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import torrent_parser as tp
# ##### in BIN folder
# data = tp.parse_torrent_file('2C12C27E904553244A6C435952CAACA257D638E5 (1).torrent')
# # See PyCharelp at https://www.jetbrains.com/help/pycharm/
# import requests
# from hashlib import sha1
# from urllib import parse
# info_hash = sha1(tp.encode(data['info']))
# print(parse.quote(info_hash.hexdigest().encode('utf-8')))
# print(data['announce'])
# peer_id = '-PYTHON0001-'
# params = {
#
#     'info_hash': info_hash,
#     'peer_id': peer_id,
#     'left': 10000,
#     'compact': 1,
#     'port': 6881,
#     'uploaded': 0,
#     'downloaded': 0,
#     'event': 'started'
# }
# r = requests.get('http://explodie.org:6969/announce', params=params)
# print(r.url)
# print(r.text)
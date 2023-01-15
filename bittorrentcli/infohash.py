# import sys, os, hashlib, bencode
# from io import  StringIO
#
# import torrent_parser
#
#
# def pieces_generator(info):
#     """Yield pieces from download file(s)."""
#     piece_length = info['piece length']
#     if 'files' in info: # yield pieces from a multi-file torrent
#         piece = ""
#         for file_info in info['files']:
#             path = os.sep.join([info['name']] + file_info['path'])
#             print(path)
#             sfile = open(path, "rb")
#             while True:
#                 piece += sfile.read(piece_length-len(piece))
#                 if len(piece) != piece_length:
#                     sfile.close()
#                     break
#                 yield piece
#                 piece = ""
#         if piece != "":
#             yield piece
#     else: # yield pieces from a single file torrent
#         path = info['name']
#         print(path)
#         sfile = open(path.decode('UTF-8'), "rb")
#         while True:
#             piece = sfile.read(piece_length)
#             if not piece:
#                 sfile.close()
#                 return
#             yield piece
#
# def corruption_failure():
#     """Display error message and exit"""
#     print("download corrupted")
#     exit(1)
#
# def main():
#     # Open torrent file
#     metainfo = torrent_parser.parse_torrent_file('B8E247869E0EA480336F41A9FDF63B4BF8FF7C50.torrent')
#     info = metainfo['info']
#     pieces = StringIO(info['pieces'])
#     # Iterate through pieces
#     for piece in pieces_generator(info):
#         # Compare piece hash with expected hash
#         piece_hash = hashlib.sha1(piece).digest()
#         if (piece_hash != pieces.read(20)):
#             corruption_failure()
#     # ensure we've read all pieces
#     if pieces.read():
#         corruption_failure()
#
# if __name__ == "__main__":
#     main()
# # Share
# Edit
# Follow
# edited Nov 15, 2010 at 22:28
# answered Apr 4, 2010 at 5:59
# user avatar
# Alex Jasmin
# 38.5k77 gold badges7676 silver badges6464 bronze badges
# Don't know if this solved the OP's problem, but it definitely solved mine (once I got past the bencode package's brokenness: stackoverflow.com/questions/2693963/…). Thanks! –
# Nicholas Knight
#  Apr 25, 2010 at 16:27
# I always wanted to have such a tool, and was about to dig into the old official python client to find out how to write one. Thanks!! –
# netvope
#  May 28, 2010 at 1:08
# Thank you very much. This functionality is available in most BitTorrent clients with GUI, with the Force Re-Check option or similar. I thought you could extract or calculate the hash (md5, sha1, whatever) for all files inside the torrent BEFORE downloading them, but apparently that's not possible unless the .torrentfile includes such metadata, which is not mandatory. –
# Smeterlink
#  Aug 20 at 12:02
# Take into account that this script is for python2, so you need to install python-pip instead of default python3-pip to get it working, also run pip2 install bencode. To launch the script run python2 yourscript.py file.torrent. Will output error only if such otherwise no specific info only the name of the file being tested. –
# Smeterlink
#  Aug 20 at 12:20
# Add a comment
#
# 17
#
# Here how I've extracted HASH value from torrent file:

#!/usr/bin/python

import sys, os, hashlib
import bencode

import torrent_parser


def main():
    # Open torrent file
    torrent_file = 'B8E247869E0EA480336F41A9FDF63B4BF8FF7C50.torrent'
    metainfo = torrent_parser.parse_torrent_file(torrent_file)
    info = metainfo['info']
    print(hashlib.sha1(torrent_parser.encode(info)).hexdigest())

if __name__ == "__main__":
    main()
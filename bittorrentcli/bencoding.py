# integer : i<num>e
# string : len:<string>
# list : i<becodded valur>e
# example  i4:spam4:eggs = ["spam,"eggs"]
# dictionary: d<bencodedstring><bencodedelement>e
# example  d3:cow4:moo4:spam4:eggs = {"cow":"moo","spam":"eggs"}

def ben_integer(n : str):
    ref=0
    ans=[]
    num = ""
    index = 0
    for i in range(ref,len(n)-1):
        if n[i]=='i' and n[i+1].isnumeric():
            index=i+1
            while n[index] != 'e':
                num += n[index]
                index += 1
            ans.append(int(num))
            num=''
    return ans
import bencode
h = bencode.bdecode('d8:announce32:udp://tracker.ccc.de:80/announce13:announce-listll32:udp://tracker.ccc.de:80/announceel35:udp://tracker.istole.it:80/announceel38:udp://tracker.publicbt.com:80/announceel44:udp://tracker.openbittorrent.com:80/announceel42:udp://tracker.torrentbox.com:2710/announceel43:http://tracker.torrentbox.com:2710/announceel35:udp://tracker.istole.it:80/announceel33:http://tracker.istole.it/announceel38:udp://tracker.publicbt.com:80/announceel36:http://tracker.publicbt.com/announceel28:http://11.rarbg.com/announceel37:http://fr33dom.h33t.com:3310/announceel37:http://tracker.xpear.de:6969/announceel28:http://10.rarbg.com/announceel31:http://tracker.prq.to./announceel43:udp://fr33domtracker.h33t.com:3310/announceee7:comment61:Torrent downloaded from torrent cache at http://itorrents.org10:created by13:uTorrent/202013:creation datei1275942908e8:encoding5:UTF-84:infod6:lengthi1728e4:name34:Madhouse (Prince) - 08 - Eight.mp312:piece lengthi65536e6:pieces20:��=��`�;�**)�5�#�ee')
import hashlib
print(hashlib.sha256(
    bencode.bencode(h['info']).encode('utf-8')
).hexdigest())
print(bencode.bencode(h['info']))

import requests
import json
import time




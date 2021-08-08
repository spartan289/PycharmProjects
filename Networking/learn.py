import requests
x = requests.get('https://www.youtube.com/watch?v=Dp6lbdoprZ0')
open('video.html','wb').write(x.content)
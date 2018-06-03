#开启Socket客户端

import sys
import time
import socket
from PIL import Image

if (1 == len(sys.argv)):
    HOST, PORT = '127.0.0.1', 9999
elif (2 == len(sys.argv)):
    HOST, PORT = sys.argv[1], 9999
elif (3 <= len(sys.argv)):
    HOST, PORT = sys.argv[1], int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST, PORT))
    data = Image.open('image.jpg')
    start_time = time.time()
    s.sendall(data.tobytes())
    reply = s.recv(1024)
    use_time = time.time() - start_time
    print('{} elapsed time: {:.3f}s'.format(time.time(), use_time))
    print('reply =', str(reply, 'utf8'))
finally:
    s.close()

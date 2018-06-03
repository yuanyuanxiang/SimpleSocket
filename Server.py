#开启Socket服务端

import sys
import socketserver
from PIL import Image

# 每次收取定长数据
SIZE = 160
max_len = SIZE*SIZE*3

class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print ('start running.')
        recv_len = 0
        recv_buf = b''
        while True:
            try:
                data = self.request.recv(max_len - recv_len)
                if (b'' == data):
                    self.request.close()
                    break
                recv_len = recv_len + len(data)
                recv_buf = recv_buf + data
                print('recv_len =', recv_len)
                if max_len == recv_len:
                    print ('Received from:', self.client_address[0])
                    image = Image.frombuffer('RGB', (SIZE, SIZE), recv_buf, 'raw', 'RGB', 0, 1)
                    image.show()
                    recv_len = 0
                    recv_buf = b''
                    self.request.sendall(bytes('Processing OK.', 'utf8'))
            except KeyboardInterrupt:
                print('Ctrl+C is pressed.')
                break
        print ('stop running.')

if __name__ == '__main__':
    if (1 == len(sys.argv)):
        HOST, PORT = '127.0.0.1', 9999
    elif (2 == len(sys.argv)):
        HOST, PORT = sys.argv[1], 9999
    elif (3 <= len(sys.argv)):
        HOST, PORT = sys.argv[1], int(sys.argv[2])
    server = socketserver.ThreadingTCPServer((HOST, PORT), RequestHandler)
    print('Start server: host =', HOST, 'PORT =', PORT)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('Ctrl+C is pressed.')
        sys.exit(0)

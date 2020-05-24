import socketserver 

class TCPRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        self.data - self.request.recv(1024).strip()
        print ("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data)

tcp_server = socketserver.TCPServer( ("",8090),TCPRequestHandler)
tcp_server.serve_forever()

import socketserver
import numpy as np
from PIL import Image

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        x=[]
        m=1
        total_data_length=0
        while 1:
            self.data = self.request.recv(int(1024)).strip()
            if not self.data: break      
            #print("{} wrote:".format(self.client_address[0]))
            #print(self.data.hex())
            x = np.append(x, self.data)
            #print (i,") data Type:", type(self.data), " Data Length: ", len(self.data))
            #conn.send("Echo".encode())  # echo
            self.request.send("Echo".encode())##
            m=m+1
            total_data_length=total_data_length+len(self.data)
            
        print("Total payload byte size: ",total_data_length)
        print("Number of packets: ",m-1)

        with open('encoded_BYTE.txt', 'wb') as f:
            y=bytes(x)
            f.write(y)
                                                    
if __name__ == "__main__":
    HOST, PORT = '192.168.1.154', 44300

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    print("[-] HOST " + str(HOST)+":"+str(PORT))
    
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

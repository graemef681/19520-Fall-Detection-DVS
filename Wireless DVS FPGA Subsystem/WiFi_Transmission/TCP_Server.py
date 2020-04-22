#!/usr/bin/env python

import socket
import numpy as np
from PIL import Image

TCP_IP = '192.168.1.154'
#TCP_IP = '192.168.43.68'

TCP_PORT = 44300
BUFFER_SIZE = 1024  # Normally 1024
print ('Buffer size ',BUFFER_SIZE)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket
s.bind((TCP_IP, TCP_PORT))
print("[-] Socket Bound to port " + str(TCP_PORT))

s.listen()
print ('Listening')

x=[] # Array used to store each packet send by the Client, this array will hold the entire info needed to create the image

conn, addr = s.accept()
print ('Connection address:', addr)
i=1
total_data_length=0 # This should be equal to the number of bytes of the image frame sent via WiFi from the Client
while 1:
    data = conn.recv(BUFFER_SIZE) # Receive one packet
    if not data: break
    x = np.append(x, data)
    #print (i,") Data Type:", type(data), " Data Length: ", len(data)) #Uncomment this to see info about each received packet from the Client
    conn.send("R".encode())  # Send ACK to Client
    i=i+1
    total_data_length=total_data_length+len(data)
#conn.close() # The client will terminate the connection before this line is called so the server's FIN request is never received by the client
print("Total payload byte size: ",total_data_length) # = Height * Width * Channels
print("Number of packets: ",i-1) # Should be equal to Image size/BUFFER_SIZE if there are no retransmitted or lost TCP packets
print("END OF WiFi Transmission")


# Reconstruct the image
print("Reconstructing the image")
Test_image=Image.new('RGB',(640,640)) 
img = Test_image.load()
y=x.tobytes() # x is an array of array bytes, this converts it to an array of bytes of shape [(B,G,R),(B,G,R),...(B,G,R)]
              # where the length is equal to the number of bytes of the received image
k=0
for i in range(0,640):
    for j in range(0,640):
        img[(j,i)] = (y[k+2],y[k+1],y[k]) # R G B
        k=k+3

Test_image.save('foo.png','png')

"""
# This is used for debugging to check the first column of the image
stride = 640 * 3
for i in range(0,640):
    print("Row ",i," First column " ,hex(y[0+stride*i]))
    """

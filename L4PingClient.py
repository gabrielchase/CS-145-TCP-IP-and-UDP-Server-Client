import socket
import time

# Create a UDP socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = b'This is the message.  It will be repeated.'


for i in range(1, 4):
    # Send data
    start_time = time.time()
    send_data = '{}'.format(i).encode()
    sent = clientsocket.sendto(send_data, server_address)

    # Receive response
    received_data, server = clientsocket.recvfrom(4096)
    received_data = received_data.decode()
    print("Received: ", received_data)
    if received_data == str(i):
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Complete in: ", elapsed_time)
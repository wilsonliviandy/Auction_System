import socket
import random
import json

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '192.168.0.101'
server_port = 10001
buffer_size = 4096

node_id = random.randint(1, 100000)
message = json.dumps({"node_id": node_id})

client_socket.sendto(message.encode('utf-8'), (server_address, server_port))
print('Sent to server:', message)

print('Waiting for response...')
data, server = client_socket.recvfrom(buffer_size)
print('Received message from server:', data.decode('utf-8'))

client_socket.close()

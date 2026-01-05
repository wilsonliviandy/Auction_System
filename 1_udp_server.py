import socket
import json

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = '192.168.0.101'
server_port = 10001
buffer_size = 1024

group_view = set()

server_socket.bind((server_address, server_port))
print('Server up and running at {}:{}'.format(server_address, server_port))
print("Listening for clients")

client_response = 'You are now listed!'

while True:
    data, address = server_socket.recvfrom(buffer_size)

    msg = json.loads(data.decode('utf-8'))
    node_id = msg["node_id"]
    group_view.add(node_id)

    print("New client found : ", node_id)
    print("Group view :", group_view)
    
    if data:
        server_socket.sendto(client_response.encode('utf-8'), address)
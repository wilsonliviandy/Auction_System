import socket
import datetime

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server application IP address and port
server_address = '127.0.0.1'
server_port = 10001

# Buffer size
buffer_size = 1024

# Bind socket to port
server_socket.bind((server_address, server_port))
print('Server up and running at {}:{}'.format(server_address, server_port))

while True:
    print('\nWaiting to receive message...\n')
    data, address = server_socket.recvfrom(buffer_size)
    client_message = data.decode('utf-8').strip()

    print('Received message from client: ', address)
    print('Message: ', client_message)
    
    if data:
        try:
            number = int(client_message)
            squared = number ** 2
            timestamp = datetime.datetime.now()
            message = f'{squared} | Server time: {timestamp}'
        except ValueError:
            message = f'Invalid input "{client_message}"'

        server_socket.sendto(message.encode('utf-8'), address)
        print('Replied to client: ', message)

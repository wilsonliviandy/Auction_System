import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
server_address = '127.0.0.1'
server_port = 10001

# Buffer size
buffer_size = 4096

# Message to send
message = 'Hi server!'

# Send data
client_socket.sendto(message.encode('utf-8'), (server_address, server_port))
print('Sent to server:', message)

# Receive response
print('Waiting for response...')
data, server = client_socket.recvfrom(buffer_size)
print('Received message from server:', data.decode('utf-8'))

# Close socket
client_socket.close()

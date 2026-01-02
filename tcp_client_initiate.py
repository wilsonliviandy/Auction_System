import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server address and port
server_address = '127.0.0.1'
server_port = 10002  # must match server

# Connect to the server
client_socket.connect((server_address, server_port))
print(f"Connected to server at {server_address}:{server_port}")

# Send message
message = "Hi server!"
client_socket.send(message.encode('utf-8'))
print(f"Sent to server: {message}")

# Receive response
data = client_socket.recv(1024).decode('utf-8')
print(f"Received from server: {data}")

# Close socket
client_socket.close()

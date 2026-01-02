import socket
import threading
import os

# Server address and port
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 10001
BUFFER_SIZE = 1024

# Function to handle each client message
def handle_client(data, client_address, server_socket):
    print(f"Received '{data.decode()}' from {client_address[0]}:{client_address[1]}")
    message = f"Hi {client_address[0]}:{client_address[1]}. Server PID {os.getpid()}"
    server_socket.sendto(message.encode(), client_address)
    print(f"Sent to client: {message}")

# Main server code
if __name__ == "__main__":
    # Create UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((SERVER_ADDRESS, SERVER_PORT))
    print(f"Server up and running at {SERVER_ADDRESS}:{SERVER_PORT}")

    while True:
        # Receive message from client
        data, address = server_socket.recvfrom(BUFFER_SIZE)
        # Start a new thread to handle this client
        client_thread = threading.Thread(target=handle_client, args=(data, address, server_socket))
        client_thread.start()

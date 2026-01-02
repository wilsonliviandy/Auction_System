import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server address and port
server_address = '127.0.0.1'
server_port = 10002  # different port from UDP

# Bind socket
server_socket.bind((server_address, server_port))
server_socket.listen(1)  # listen for incoming connections
print(f"TCP Server listening on {server_address}:{server_port}...")

while True:
    print("\nWaiting for a client to connect...")
    conn, addr = server_socket.accept()  # accept new connection
    print(f"Connected to client: {addr}")

    try:
        data = conn.recv(1024).decode('utf-8').strip()  # receive data
        if data:
            print(f"Received from client: {data}")
            message = "Hi client! Nice to connect with you over TCP!"
            conn.send(message.encode('utf-8'))  # send reply
            print(f"Replied to client: {message}")
    finally:
        conn.close()  # close the connection after one exchange

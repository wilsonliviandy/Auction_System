import socket

BROADCAST_PORT = 5973

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind(("0.0.0.0", BROADCAST_PORT))

group_view = set()

print("Listening to broadcast announcements")

while True:
    data, addr = listen_socket.recvfrom(1024)

    sender_ip = addr[0]
    group_view.add(sender_ip)

    print("Received from:", sender_ip)
    print("All known senders:", group_view)

import socket
import multiprocessing
import os

def send_message(s_address, s_port, task_number):
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Message sent to server
    message = str(task_number)
    
    # Send data
    client_socket.sendto(message.encode(), (s_address, s_port))
    print(f'Client {os.getpid()} sent: {message}')
    
    # Receive response from server
    data, server = client_socket.recvfrom(1024)
    print(f'Client {os.getpid()} received: {data.decode()}')
    
    # Close the socket
    client_socket.close()

if __name__ == '__main__':
    # Server application IP address and port
    server_address = '127.0.0.1'
    server_port = 10001

    processes = []

    # Spawn three client processes
    for i in range(1, 6):
        p = multiprocessing.Process(target=send_message, args=(server_address, server_port,i))
        p.start()
        processes.append(p)

    # Wait for all processes to finish
    for p in processes:
        p.join()

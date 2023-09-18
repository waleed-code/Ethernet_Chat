import socket
import threading

def receive_messages(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        print("server :", data)

    # Close the client socket
    client_socket.close()

# Set up the client
HOST = '192.168.32.108'  # Server IP address
PORT = 12345        # Server port number

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Start a new thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

while True:
    # Send a message to the server
    message = input()
    client_socket.sendall(message.encode())

    # Break the loop if the user wants to exit
    if message.lower() == 'exit':
        break

# Close the client socket
client_socket.close()
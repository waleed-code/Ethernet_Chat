import socket
import threading

def process_message(message):
    # Add your chatbot logic here
    response = message
    return response

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        print("client :",data)

        # Process the received message
        response = process_message(data)

        # Send the response back to the client
        client_socket.sendall(response.encode())

    # Close the client connection
    client_socket.close()

def send_messages(client_socket):
    while True:
        message = input()
        client_socket.sendall(message.encode())

# Set up the server
HOST = '192.168.32.108'  # Server IP address
PORT = 12345        # Server port number

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print("Chatbot server is running...")

# Accept a client connection
client_socket, addr = server_socket.accept()
print("Connected to", addr)

# Start a new thread to handle the client
client_thread = threading.Thread(target=handle_client, args=(client_socket,))
client_thread.start()

# Start a new thread to send messages to the client
send_thread = threading.Thread(target=send_messages, args=(client_socket,))
send_thread.start()
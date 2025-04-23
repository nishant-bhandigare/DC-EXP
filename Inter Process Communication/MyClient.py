import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect(("192.168.20.92", 6666))  # Your server's IP
client_socket.connect(("127.0.0.1", 6666))  # Use localhost instead
print("Connected to the server. Type 'exit' to quit.")

while True:
    message = input("Enter command: ")  # Take user input
    client_socket.send(message.encode())  # Send data
    if message.lower() == "exit":
        break
    response = client_socket.recv(1024).decode()  # Receive response
    print(f"Server: {response}")

client_socket.close()  # Close connection

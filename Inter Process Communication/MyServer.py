import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 6666))  # Listen on all interfaces
server_socket.listen(5)  # Allow multiple connections
print("Server is running... Waiting for connections.")

while True:
    conn, addr = server_socket.accept()  # Accept incoming connection
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024).decode()  # Receive data
        if not data or data.lower() == "exit":  # Stop if "exit" is received
            print("Closing connection.")
            break

        print(f"Received: {data}")
        response = input("Enter response: ")  # Take server input
        conn.send(response.encode())  # Send response back to client
    conn.close()  # Close client connection

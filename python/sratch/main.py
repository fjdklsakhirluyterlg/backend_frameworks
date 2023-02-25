import socket

PORT = 5030
BUFFER_SIZE = 1024
HOST = ''

def handle_request(client_socket):
    request = client_socket.recv(BUFFER_SIZE).decode()

    print(request)

    request_lines = request.split('\r\n')
    path = request_lines[0].split()[1]

    response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nHello, World!"

    client_socket.sendall(response.encode())

    client_socket.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))

    # Listen for incoming connections
    server_socket.listen()

    print(f"Server listening on port {PORT}")

    while True:
        # Accept a new client connection
        client_socket, address = server_socket.accept()

        # Handle the client's request
        handle_request(client_socket)
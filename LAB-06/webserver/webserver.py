import socket

def handle_request(client_socket, request_data):
    print(f"Received request:\n{request_data}")  # Debug request đầu vào

    if request_data.startswith("GET /admin"):
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Welcome to the admin page!</h1>"
    else:
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>This is a simple website!</h1>"

    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5000))  # Cổng 5000
    server_socket.listen(5)
    print("Server listening on port 5000...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        request_data = client_socket.recv(1024).decode('utf-8')
        print(f"Received request:\n{request_data}")  # Debug request nhận được
        handle_request(client_socket, request_data)

if __name__ == "__main__":
    main()
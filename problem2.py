import socket
import threading

# Define the backend servers (IP address and port)
backend_servers = [
    ("127.0.0.1", 8001),
    ("127.0.0.1", 8002),
    ("127.0.0.1", 8003),
    ("127.0.0.1", 8004)
]

# This class implements the load balancer
class LoadBalancer:
    def __init__(self, host, port, backend_servers):
        self.host = host
        self.port = port
        self.backend_servers = backend_servers
        self.current_server = 0
        self.lock = threading.Lock()

    def start(self):
        # Create a socket to listen for incoming connections
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen()
            print(f"Load balancer listening on {self.host}:{self.port}")

            while True:
                # Accept a new connection
                client_socket, client_address = server_socket.accept()
                print(f"Connection from {client_address}")
                # Handle the connection in a new thread
                threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        # Get the next backend server to forward the request to
        backend_server = self.get_next_server()

        try:
            # Create a socket to connect to the backend server
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as backend_socket:
                backend_socket.connect(backend_server)
                # Start threads to forward data between client and backend server
                threading.Thread(target=self.forward, args=(client_socket, backend_socket)).start()
                self.forward(backend_socket, client_socket)
        except Exception as e:
            print(f"Error connecting to backend server: {e}")
        finally:
            client_socket.close()

    def forward(self, source, destination):
        try:
            while True:
                # Receive data from the source
                data = source.recv(4096)
                if not data:
                    break
                # Send the data to the destination
                destination.sendall(data)
        except Exception as e:
            print(f"Error forwarding data: {e}")
        finally:
            source.close()
            destination.close()

    def get_next_server(self):
        with self.lock:
            # Get the next server in the list
            server = self.backend_servers[self.current_server]
            # Move to the next server (round-robin)
            self.current_server = (self.current_server + 1) % len(self.backend_servers)
        return server

# Define the load balancer's listening address and port
load_balancer = LoadBalancer("127.0.0.1", 8000, backend_servers)
# Start the load balancer
load_balancer.start()

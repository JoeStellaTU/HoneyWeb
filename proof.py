import socket
import threading

def handle_connection(client_socket):
    # This function handles the incoming connection and simulates a response
    response = "Welcome to the honeypot!\nUsername: "
    client_socket.send(response.encode())
    
    # You can log the interaction or perform further analysis here
    
    # Close the connection
    client_socket.close()

def start_honeypot(bind_ip, bind_port):
    # Create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to a specific IP and port
    server.bind((bind_ip, bind_port))
    
    # Listen for incoming connections
    server.listen(5)
    
    print(f"[*] Listening on {bind_ip}:{bind_port}")
    
    while True:
        # Accept incoming connection
        client, addr = server.accept()
        
        print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")
        
        # Handle the connection in a new thread
        client_handler = threading.Thread(target=handle_connection, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    # Set the IP and port to bind the honeypot
    honeypot_ip = "0.0.0.0"  # Listen on all available interfaces
    honeypot_port = 23  # Telnet port
    
    start_honeypot(honeypot_ip, honeypot_port)

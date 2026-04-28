# This is a self-contained port scanner
# Using sockets
# This one is done using OOP concepts

import socket
import datetime

# Self-container port scanner
class PortScanner:
    def __init__(self, hostname, low_port=21, high_port=80):
        self.hostname = hostname
        self.low_port = low_port
        self.high_port = high_port

    def scan(self):
        
        # This is to ensure IP address exists before try
        host_ip = ""

        try:
            host_ip = socket.gethostbyname(self.hostname)
        except socket.gaierror:
            print("Unable to resolve hostname")
            return # end the function
        
        # Main loop
        for port in range(self.low_port, self.high_port+1):
            # Create TCP/IPv4 socket
            sock = socket.socket()
            sock.settimeout(.5)

            try:
                sock.connect((host_ip, port))
                print(f"{host_ip} port {port}: open.")
            except KeyboardInterrupt:
                print("Scan interrupted by user.")
                return
            except TimeoutError:
                pass
            




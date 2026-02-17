# This is a "quick and dirty" clone of nmap
# The idea is to introduce Python socket programming
# And exceptions with a simple port scan program

# For the purpose of the demo we are sticking to ports
# 1 to 3389 - a better version would ask for ports, or optimise ports etc

# We need to import the socket module + time stamp
import socket
import datetime # (for timestamp purpose)

# For time issues - 21 to 80 for now 
MIN_PORT = 21
MAX_PORT = 80

# For scope, create those variables now
host_ip = ""
dns_success = False

# While DNS not resolved
while not dns_success:
    # Ask user and resolve host via DNS
    hostname = input("Enter your machine's name or IP:")
    try:
        host_ip = socket.gethostbyname(hostname)
        # Line below will only run if successful
        dns_success = True
    except socket.gaierror:
        print("Unable to resolve", hostname, "into an IP address.")
        dns_success = False

# TODO timestamp

# Main loop
for port in range(MIN_PORT, MAX_PORT+1):
    # Create a TCP/IPV4 socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(.5) # Gives up after time in seconds

    # Try to connect to ip / port
    try:
        sock.connect((host_ip, port))
        print(f"{host_ip} port {port}: open.")
    except KeyboardInterrupt:
        # User typed Ctrl-C and wants to end the program
        print("Program ended on your request.")
        exit()
    except: # Ignore other exceptions
        pass
    

# Debug
# print(host_ip)



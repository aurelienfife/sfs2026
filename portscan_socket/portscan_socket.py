# This is a "quick and dirty" clone of nmap
# The idea is to introduce Python socket programming
# And exceptions with a simple port scan program

# For the purpose of the demo we are sticking to ports
# 1 to 3389 - a better version would ask for ports, or optimise ports etc

# We need to import the socket module + time stamp
import socket
import datetime # (for timestamp purpose)

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

# Debug
print(host_ip)
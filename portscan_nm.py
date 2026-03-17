import nmap

# Create a PortScanner object
ps = nmap.PortScanner()

# Scan IP address of your choice
output = ps.scan('172.17.0.2-4')

#print(output)

# There's examples online but by looking the output
# You can 'reverse engineer' the structure
# of the object

ip_list = output['scan'].keys()
#print(ip_list)

# Go over the IP addresses
for k in ip_list:
    # List of ports
    ports = output['scan'][k]['tcp'].keys()
    
    print("IP", k)
    for p in ports:
        print("Port", p, "state", output['scan'][k]['tcp'][p]['state'])

    # commit this

# test
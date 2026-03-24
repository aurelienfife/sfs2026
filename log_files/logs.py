# 17/03 - Analyse web logs

# This will take an Apache web log (standard format)
# And reduce its data to check IP frequencies
def extract_ips(file_path):
    # First we open the file
    f = open(file_path)
    ip_addresses = []

    # In this case we can read the log line by line ->
    # The code below will assume you are reading line by line
    # Hence f.readline() not being necessary
    for line in f:
        # Cleaning up extra new line characters + split
        comp = line.strip().split() 
        # Extract IP address
        ip = comp[0]
        ip_addresses.append(ip)
    
    return ip_addresses

# This will take the list of IP addresses
# And return dictionary of the following format { "unique_ip" : count }
def count_ips(ip_list):
    # Create results dictionary
    ip_dict = { }

    # Go through IPs one-by-one
    for ip_addr in ip_list:
        # If IP already exists as a key
        # Increase value by one
        # Else create key and set value to one
        if ip_addr in ip_dict.keys():
            ip_dict[ip_addr] += 1
        else:
            ip_dict[ip_addr] = 1            

    return ip_dict

# def extract_count(ip_item):
#     # Assumer ip_item is (ip, count)
#     return ip_item[1]

def sort_ips(ip_dict):
    # Create a list of sorted IPs / count tuples
    sorted_items = []

    item_list = list(ip_dict.items())

    # We need to use a lambda
    # i.e. a function without a name
    sorted_items = sorted(item_list, key=lambda a : a[1], reverse=True)
    return sorted_items

def main():
    ip_list = extract_ips("log_files/full_log.txt")
    ip_dict = count_ips(ip_list)
    sorted_list = sort_ips(ip_dict)
    
    # Display sorted
    for item in sorted_list:
        print(item[0],":", item[1])
    


if __name__ == "__main__":
    main()

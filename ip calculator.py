import ipaddress

def calculate_ip_details(ip_with_prefix):
    try:

        network = ipaddress.IPv4Network(ip_with_prefix, strict=False)
        

        ip_address = ip_with_prefix.split('/')[0]  
        network_address = network.network_address
        broadcast_address = network.broadcast_address
        netmask = network.netmask
        wildcard_mask = network.hostmask
        host_min = list(network.hosts())[0]  
        host_max = list(network.hosts())[-1]  
        num_hosts = network.num_addresses - 2  

        # Print results
        print(f"Address:   {ip_address}           {bin(int(ipaddress.IPv4Address(ip_address)))[2:].zfill(32)}")
        print(f"Netmask:   {netmask} = {network.prefixlen:<6} {bin(int(ipaddress.IPv4Address(netmask)))[2:].zfill(32)}")
        print(f"Wildcard:  {wildcard_mask}        {bin(int(ipaddress.IPv4Address(wildcard_mask)))[2:].zfill(32)}")
        print(f"Network:   {network_address}/{network.prefixlen:<10} {bin(int(ipaddress.IPv4Address(network_address)))[2:].zfill(32)}")
        print(f"Broadcast: {broadcast_address}    {bin(int(ipaddress.IPv4Address(broadcast_address)))[2:].zfill(32)}")
        print(f"HostMin:   {host_min}             {bin(int(ipaddress.IPv4Address(host_min)))[2:].zfill(32)}")
        print(f"HostMax:   {host_max}             {bin(int(ipaddress.IPv4Address(host_max)))[2:].zfill(32)}")
        print(f"Hosts/Net: {num_hosts}                   (Private Internet)" if network.is_private else "(Public Internet)")

    except ValueError as e:
        print(f"Error: {e}")


ip_with_prefix = input("Enter an IP address with prefix (e.g., 192.168.0.1/24): ")
calculate_ip_details(ip_with_prefix)

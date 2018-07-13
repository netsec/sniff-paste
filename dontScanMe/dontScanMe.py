from ipaddress import IPv4Address as IPv4
from ipaddress import IPv4Network as IPv4Net

def isFiltered(ip):
    with open("nmapfilter.conf") as ipFilters:
        for networkString in ipFilters:
            ip=IPv4(ip)
            network=IPv4Net(networkString.rstrip("\r\n")) 
            if(ip in network):
                return True
    return False    




ips= ["192.168.1.1","0.0.0.0","1.0.0.3","192.168.1.20"]


for ip in ips:
    if(isFiltered(ip)):
        print(ip+" is blocked, do not scan")
    else:
        print(ip+" is free! Scan away")

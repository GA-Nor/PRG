
"""
# TASK 1 — SUSPICIOUS IP ADDRESS CHECKER

1. Create a list containing at least five observed IP addresses.
2. Create another list containing at least three suspicious IP addresses.
3. Use a `for` loop to check each observed IP address.
4. Use `if` and `else` to print `SUSPICIOUS` or `SAFE`.
5. Create a counter for suspicious IP addresses.
6. Print the counter at the end.


Expected output:


192.168.1.10 - SAFE
10.0.0.5 - SAFE
203.0.113.50 - SUSPICIOUS
192.168.1.20 - SAFE
198.51.100.15 - SUSPICIOUS

Total suspicious IPs: 2


Extra challenge

Create a `check_ip()` function that receives an IP address and returns `True` or `False`.


This is the same task as Week1 - Task 3-1, but we read addresses from a file instead.
"""

def check_ips(okList, suspList):
    suspiciousCounter = 0
    for ip in okList:
        if ip in suspList:
            print(f"{ip} - Suspicious")
            suspiciousCounter += 1
        else:
            print(f"{ip} - OK")
    
    print(f"Total number of suspicious IP's: {suspiciousCounter}")

def create_list(ipList):
    
    tempList = []
    
    with open(ipList, "r") as file:

        for line in file:
            ip = line.strip()
            if ip != "":
                tempList.append(ip)

    return tempList



ip_addresses = create_list()
suspicious_ips = create_list()

#Then we simple call the function
check_ips(ip_addresses, suspicious_ips)

print(len(ip_addresses))
print(len(suspicious_ips))
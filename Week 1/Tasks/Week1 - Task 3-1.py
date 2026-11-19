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


"""

ip_addresses = [
    "192.168.1.10",
    "10.0.0.5",
    "203.0.113.50",
    "192.168.1.20",
    "198.51.100.15"
]

suspicious_ips = [
    "203.0.113.50",
    "198.51.100.15",
    "10.0.0.99"
]

ipa = []
with open("network_ips.txt", "r") as file:

        for line in file:
            ip = line.strip()

            if ip != "":
                ipa.append(ip)

ipsusp = []
with open("suspicious_ips.txt", "r") as file:

        for line in file:
            ip = line.strip()

            if ip != "":
                ipsusp.append(ip)

print(len(ipa))
print(len(ipsusp))
# TODO 1: Create a counter for suspicious IP addresses.
#counter

# TODO 2: Use a for loop to examine the addresses in ip_addresses.

#use a for loop that goes through each ip address

# TODO 3: Use if/else and print SAFE or SUSPICIOUS, increase counters.
    #Condition: check if the current ip address is in the list of suspicious ip addresses
        #print the ip address, with the text "Suspicious"
        # increase the suspicious counter by 1
    #if its not the case, print the ip address and the text "Safe"


#Print the total number of suspicious ip addresses. 

# Run from the task_1_easy folder or use this standalone solution.
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

suspicious_count = 0

for ip_address in ip_addresses:
    if ip_address in suspicious_ips:
        print(ip_address, "- SUSPICIOUS")
        suspicious_count = suspicious_count + 1
    else:
        print(ip_address, "- SAFE")

print()
print("Total suspicious IPs:", suspicious_count)

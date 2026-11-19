import csv

def check_connection(port, data_mb, blocked):
    special_port = False

    if port == 21 or port == 22 or port == 3389:
        special_port = True

    if blocked == True and special_port == True:
        return True
    elif data_mb > 500:
        return True
    else:
        return False


source_ips = []
suspicious_ips = []
total_connections = 0
blocked_connections = 0
suspicious_connections = 0
total_data = 0.0

print("NETWORK TRAFFIC ANALYZER")
print("----------------------------------------")

with open("network_traffic.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        source_ip = row["source_ip"]
        source_ip = source_ip.strip()
        port = int(row["port"])
        data_mb = float(row["data_mb"])

        blocked_text = row["blocked"]
        blocked_text = blocked_text.strip()
        blocked_text = blocked_text.lower()
        if blocked_text == "true":
            blocked = True
        else:
            blocked = False

        source_ips.append(source_ip)
        total_connections = total_connections + 1
        total_data = total_data + data_mb

        if blocked == True:
            blocked_connections = blocked_connections + 1

        suspicious = check_connection(port, data_mb, blocked)
        if suspicious == True:
            suspicious_connections = suspicious_connections + 1
            suspicious_ips.append(source_ip)
            print(source_ip, "Port:", port, "SUSPICIOUS")
        else:
            print(source_ip, "Port:", port, "NORMAL")

print()
print("SUMMARY")
print("----------------------------------------")
print("Total connections:", total_connections)
print("Blocked connections:", blocked_connections)
print("Suspicious connections:", suspicious_connections)
print("Total data transferred:", round(total_data, 1), "MB")
print("Suspicious IP addresses:")
for ip_address in suspicious_ips:
    print(ip_address)

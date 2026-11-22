def process_device(record):
    parts = record.strip().split(",")
    device_name = parts[0].title()
    ip_address = parts[1].strip()
    status = parts[2].strip().title()
    return device_name, ip_address, status


def load_devices(filename):
    devices = {}
    with open(filename) as file:
        for line in file:
            device_name, ip_address, status = process_device(line)
            devices[ip_address] = {
                "device": device_name,
                "status": status
            }
    return devices


def device_statistics(device_dict):
    online_count = 0
    offline_count = 0

    for device in device_dict.values():
        if device["status"] == "Online":
            online_count += 1
        elif device["status"] == "Offline":
            offline_count += 1

    total_devices = len(device_dict)
    return total_devices, online_count, offline_count


devices = load_devices("devices.csv")
total_devices, online_count, offline_count = device_statistics(devices)

online_devices = set()
for device in devices.values():
    if device["status"] == "Online":
        online_devices.add(device["device"])

print("Device inventory")
print("IP address".ljust(20) + "Device".ljust(20) + "Status")
print("-" * 50)
for ip_address in sorted(devices):
    device = devices[ip_address]
    print(ip_address.ljust(20) + device["device"].ljust(20) + device["status"])

print("Total devices:", total_devices)
print("Online devices:", online_count)
print("Offline devices:", offline_count)
print("Devices currently online:")
for device_name in sorted(online_devices):
    print(device_name)

search_ip = input("Enter an IP address to look up: ")
if search_ip in devices:
    print("Device found:", devices[search_ip])
else:
    print("No device found for that IP address.")

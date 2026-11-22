def process_device(record):
    try:
        parts = record.split(",")
        device_name = parts[0].strip()
        ip_address = parts[1].strip()
        status = parts[2].strip().lower()
    except IndexError:
        return "ERROR: Missing field"

    if device_name == "" or ip_address == "":
        return "ERROR: Missing field"

    if status not in ["online", "offline"]:
        return "ERROR: Invalid status"

    return device_name, ip_address, status

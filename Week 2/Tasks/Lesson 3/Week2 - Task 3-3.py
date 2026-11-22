"""
Task 3 - Device Inventory Validator

Each device record contains a device name, an IP address, and a status,
separated by commas:
"laptop,192.168.1.10,online"

Create a function called process_device(record) that:
1. Splits the record into its three fields.
2. Removes extra spaces around each field.
3. Changes the status to lowercase so that "ONLINE" is treated as "online".
4. Checks that all three fields are present and that the device name and
   IP address are not empty.
5. Allows only "online" or "offline" as a status.
6. Returns the device name, IP address, and status together as a tuple
   when the record is valid.

Handle these errors by returning the indicated message:
- A field is missing, or the device name or IP address is empty:
  "ERROR: Missing field"
- The status is not "online" or "offline":
  "ERROR: Invalid status"

Try the function with each device below. Valid records should return a
tuple; invalid records should return an error message.
"""

devices = [
    "laptop,192.168.1.10,online",
    "server,192.168.1.20",
    "phone,192.168.1.30,active",
    "tablet,192.168.1.40,offline",
]

# TODO: Create process_device(record) to validate and process one device record.

"""
TASK 3 - NETWORK TRAFFIC ANALYZER
Read TASK.md before starting.

## Part A - Load and process data

1. Read `network_traffic.csv` with `csv.DictReader()`.
2. Extract `source_ip`, `port`, `data_mb` and `blocked`.
3. Convert `port` to an integer and `data_mb` to a float.
4. Convert the blocked text (`True`/`False`) to a Python boolean using an explicit `if` / `else`.
5. Save each source IP address in a list.

## Part B - Security rules

Create a function `check_connection(port, data_mb, blocked)` that returns `True` when **either** of these conditions is met:
    - The connection is blocked **and** uses port 21, 22 or 3389.
    - The connection transferred **more than** 500 MB.

Otherwise return `False`. Use `if`, `elif` or `else` and logical operators.

## Part C - Report

1. Print source IP, port and whether each connection is `SUSPICIOUS` or `NORMAL`.
2. Count all connections, blocked connections, and suspicious connections.
3. Add up the data transferred (MB).
4. Store the suspicious source IPs in a separate list.
5. Print summary totals and the suspicious IP addresses at the end.

## Expected summary

Total connections: 8
Blocked connections: 3
Suspicious connections: 4
Total data transferred: 1787.0 MB


The suspicious IP addresses should be: `10.0.0.15`, `203.0.113.10`, `192.168.1.30`, `203.0.113.50`.

## Extra challenge

Write a function that classifies traffic as:

- LOW: less than 10 MB
- MEDIUM: 10 MB to 500 MB (inclusive)
- HIGH: more than 500 MB

Print the category for each connection.

"""
import csv

# TODO 1: Write check_connection(port, data_mb, blocked).
# Return True for suspicious connections; otherwise return False.


source_ips = []
suspicious_ips = []
total_connections = 0
blocked_connections = 0
suspicious_connections = 0
total_data = 0.0

print("NETWORK TRAFFIC ANALYZER")
print("----------------------------------------")

# TODO 2: Open network_traffic.csv and read the records.

# TODO 3: Convert the types of the CSV fields.

# TODO 4: Update the lists and counters.

# TODO 5: Call check_connection and print each result.

print()
print("SUMMARY")
print("----------------------------------------")
# TODO 6: Print all totals and suspicious IP addresses.

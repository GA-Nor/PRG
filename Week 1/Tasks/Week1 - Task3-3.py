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

def check_connection(port, data_mb, blocked):
    #create a special port Bool, that we can set to True if the port is a special port

    #Condition: if the port parameter is either 21, 22 or 3389, then set the special port Bool to True

    #Condition: if the blocked parameter is True, AND the special port is true, then return the value true
    #However, if one of them are False, but the data_md parameter is more than 500, return the value true
    #but if none of the conditions are met, return the value false
    



source_ips = []
suspicious_ips = []
total_connections = 0
blocked_connections = 0
suspicious_connections = 0
total_data = 0.0

print("NETWORK TRAFFIC ANALYZER")
print("----------------------------------------")

# TODO 2: Open network_traffic.csv and read the records.

with open("network_traffic.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    
# TODO 3: Convert the types of the CSV fields.
    
    #use a for-loop to go through each row in the reader dictionary
        #To see the header/fieldnames, you can look at the first line in the dataset (network_traffic.csv), use these headers to extract the data
        
        #store the source ip from the current row in a variable
        #string any whitespaces from the source ip, just in case
        
        #store the port (a number) from the current row 
        
        #Store the amount of traffic (a number) specified in the current row (you can find this in the first line of the dataset)
        
        #Store the blocked text from the current rock in a variable
        #strip whitespaces, and convert it to lower case
        #Condition: Check if the blocked text matches either true or false
            #if it does, make a variable that is set to a correct boolean value

# TODO 4: Update the lists and counters.

        #take our existing list source_ips (declared before we open the file), and append the source ip that we extracted earlier
        #increase the total_connections variable by 1, so we can track how many rows we have processed (just for presentation)
        #add the amount of traffic to our existing total_data variable
        
        #Condition: if the blocked variable of the current row is True, increase the existing blocked_connections variable by 1
        
# TODO 5: Call check_connection and print each result.
        #create a variable, "suspicious" to hold the result of our Function (check_connection) the function needs to know the port, amount of traffic and blocked status
        
        #Condition: if suspicious is true
            #increase the suspicious_connections counter by 1
            #add the source ip to the existing suspicious_ips list
            #print the source ip, port number and some text that indicate that this connection(row) is suspicious
        #if its not the case
            #print the source ip, port number and some text that tell the used this connection is ok
    
    

print()
print("SUMMARY")
print("----------------------------------------")
# TODO 6: Print all totals and suspicious IP addresses.
#print the following:
# total connections
# blocked connections
# suspicious connections
# total data transferred


# use a for-loop to print all the suspicious ips
#Import the csv module to read CSV files
import csv

# A function that flags suspicious logins based on the following:
# - was the login successfull
# - number of failed attempts
# - risk score
#We usually add functions at the top of the script to make sure they are defined before they are used.
def review_login(loginSuccess:bool, failedAtt:int, riskSc:float):
    tooManyFailures = False
    highRisk = False
    
    #Check if the login was unsuccessful and if there were 3 or more failed attempts
    if(loginSuccess == False and failedAtt >= 3):
        tooManyFailures = True
    if(riskSc >= 0.5):
        highRisk = True
    
    if(tooManyFailures or highRisk):
        return True
    else:
        return False


#initialize variables we'll use 
totalEvents = 0
failedLogins = 0
alertNames = []

#Initial presentation         
print("LOGIN SECURITY REPORT")
print("---------------------")


#Open and read the CSV file.
#the keyword "with" means that the file will be automatically closed after the indented block of code is executed.
with open("login_events.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    #print the headers for the CSV file.
    """
    for header in reader.fieldnames:
        print(header)
    
    #We are using the DictReader class, which is a dictionary containing keys and values for each row in the CSV file. The keys are the column headers, and the values are the data in each row.
    #This is what it looks like
    for row in reader:
        print(row)
        break
    for index, row in enumerate(reader, start=1):
        row["index"] = index
        print(row)
    """
    
    for row in reader:        
        #Since this loop goes through each entry, and each entry is 1 event, increment the number of events by 1 pr iteration through the loop
        totalEvents += 1
        
        # Step 1: Print the username instead of the whole row.
        #print(row["username"])
        
        # Step 3: Store the username in a variable.
        # Step 4: Clean it with strip() and title().
        username = row["username"].strip().title()
        
        # Step 5: Store failed_attempts to int.
        failedAttempts = int(row["failed_attempts"])
        
        # Step 6: Store risk_score to float.
        riskScore = float(row["risk_score"])
        
        # Step 7: Store success to True or False using if/else.
        success = row["success"].strip().lower()
        if(success == "true"):
            success = True
        else:
            success = False

        # Step 8: Add an if/else to print SUCCESS or FAILED.
        status = ""
        if(success == True):
            status = "SUCCESS"
        else:
            status = "FAILED"
            failedLogins += 1 #increase the failed logins counter by 1 if the login was unsuccessful
        print (f"Username: {username}, Status: {status}")
        
            
        # Step 9: Check if this user should be flagged, save flagged names in a list.
        reviewRequired = review_login(success, failedAttempts, riskScore)
        
        if(reviewRequired == True):
            alert_text = "Review Required" #We only use this to print the status of the login, we don't use it to flag users.            
            alertNames.append(username) #Here we add this users name to the list of alerts
        else:
            alert_text = "OK"
        
        
        # Step 10: Print totals and all flagged names.
        #print user, status, failted attempts
        #print risk score and alert status
        print(f"Users: {username} | Status: {status} | Failed attempts: {failedAttempts}")
        print(f"Risk score: {riskScore} | Alert: {alert_text}")

        
        

# Print summary numbers.
# total events
# failed logins
# events flagged

# flagged users
# for loop to print all flagged names



#Write the list of flagged users to a text file called login_report.txt
with open("login_report.txt", "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    #write the header to the text file
    writer.writerow(["Flagged Users:"])
    
    #from the list of flagged users write the username to a text file
    for user in alertNames:
        writer.writerow([user])
    
    
"""   


"""
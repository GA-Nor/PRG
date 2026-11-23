"""
Use the following methods:
.isalpha()
.isupper()
.islower()
.isdigit() 
.count()   
"""

#passwords = ["pass123", "qwerty", "abc123"]



#create solution that checks what characters a string contains
def check_password(pw=""):
    
    starts_with_letter = False
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    symbol_count = 0
    
    if(pw == "" ):
        print("invalid entry")
        return

    #check if the first char is a letter
    if(pw[0].isalpha()):
        starts_with_letter = True
    for c in pw:
        if(c.isupper()):
            uppercase_count +=1
        elif(c.islower()):
            lowercase_count +=1
        elif(c.isdigit()):
            digit_count +=1
        else:
            symbol_count +=1
     
    return starts_with_letter, uppercase_count, lowercase_count, digit_count, symbol_count
 
p ="Passw!!!!0rd"

def print_this(myVar=()):
    
    isLetter, upperCount, lowerCount, digitCount, symbolCount = t
    print(f"Entered Password: {p}")
    print("Is first char a letter?", isLetter)
    print("Uppercase count:", upperCount)
    print("Lowercase count:", lowerCount)
    print("Digit count:", digitCount)
    print("Symbol count:", symbolCount)
    print("Total length:", len(p))
    print("Letter count:", upperCount+lowerCount)


print_this(check_password(p))


#if the length of the password is more than 0, and the first character[] is alphabetic, set true

#for each character in password
    #check if the character is uppercase, if it is increment.
    #check if the character is lowercase, if it is increment.
    #check if the character is digit, if it is increment.
    #otherwise it's a symbol, increment

#print the statistics


#for each character in password 
    #if the character is a letter, 
       #print the count of the letter in the password




    


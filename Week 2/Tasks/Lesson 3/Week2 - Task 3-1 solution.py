try:
    number_text=input("Divide 100 by (a number between 1 and 100): ")
    number = int(number_text)
    
    if (number > 100):
        print("The number you entered was outside the valid range.")
    else:
        result = 100 / number
        print(result)
except ValueError:
    print("ERROR: Please enter a valid number.")
except ZeroDivisionError:
    print("ERROR: Cannot divide by zero.")

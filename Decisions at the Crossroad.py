# Task 1: Code Correction 
# You are provided with a Python script that uses 
# conditional statements to tell if a number is 
# positive, negative, or zero, but it has some errors. 
# Identify and fix them.

# Buggy Code:

# number = input("Enter a number: ")

# if number > 0:
#    print("The number is positive.")
# elif number = 0:
#    print("The number is zero.")
# else number < 0:
#    print("The number is negative.")

# Answer:
number = int(input("Enter a number: "))
# Converted the input to an integer.
if number > 0:
    print("The number is positive.")
elif number == 0: # Used == for equality comparison.
    print("The number is zero.")
else: #Corrected syntax for else statement.
    print("The number is negative.")

    
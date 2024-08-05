# Task 1: Leap Year Checker 
# Write a Python program that prompts the user to 
# input a year. The program should determine if the 
# given year is a leap year or not and then display 
# an appropriate message. Please note that this is 
# the definition of a leap year: 
# Every year that is exactly divisible by four is a 
# leap year, except for years that are exactly 
# divisible by 100, but these centurial years are 
# leap years if they are exactly divisible by 400.

#Answer:
def is_leap_year(year):
    # Check if the year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Prompt the user to input a year
year = int(input("Enter a year: "))

# Determine if the year is a leap year and display an  
# appropriate message
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#Jesse Page
#Lab 3 assignment             
#This program will take prompt the user to enter their name and birth month and year.
#The program will then output to the console a greeting with their name, 
# what season they were born, and whether or not they were born in a leap year    

def main():
    # sentinel variable
    CONTROL = "zzz"

    # Read user's name
    user_name = input("Please enter your name: ")

    # Check for the sentinal value of "zzz"
    while user_name != CONTROL:
        month = get_month()
        year = get_year()
        season = find_season(month)
        is_leap_year(user_name, season, year)
        penny_jar()
        print("Enter zzz to stop or enter another name to continue")
        user_name = input("Please enter your name: ")



def get_month():
    user_birth_month = int(input("Please enter your birth month: "))
    #input validation for birth month
    while user_birth_month <= 0 or user_birth_month > 12:
        print("Error, enter a valid birth month")
        user_birth_month = int(input("Please enter your birth month: "))
    return user_birth_month

def get_year():
    user_birth_year = int(input("Please enter your birth year: "))
    #input validation for user_birth_year
    while user_birth_year <= 0:
        print("Error, enter a valid birth year")
        user_birth_year = int(input("Please enter your birth year: "))
    return user_birth_year

def find_season(month):
    #if-else condition to check month and assign correct season
    if month <= 2:
        season = "winter"
    elif month <= 5:
        season = "spring"
    elif month <= 8:
        season = "summer"
    elif month <= 11:
        season = "fall"
    elif month == 12:
        season = "winter"
    return season

def is_leap_year(user_name, season, year):
    #if-else condition to check if user_birth_year is a leap year, and the resulting print statement
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        print("Hello,", user_name, end="")
        print("! You were born in the", season, end="")
        print(".",year, "was a leap year.")
    else:
        print("Hello,", user_name, end="")
        print("! You were born in the", season, end="")
        print(".",year, "was not a leap year.")


    # For example, if they have 589 pennies they will get:
    # 5 dollars
    # 3 quarters
    # 1 dime
    # 4 pennies
def penny_jar():
    pennies = int(input("Please enter the amount of pennies: "))
    dollars = pennies // 100
    pennies_left_dollars = pennies % 100
    print (dollars, "dollars")

    if pennies_left_dollars != 0:
        quarters = pennies_left_dollars // 25
        pennies_left_quarters = pennies_left_dollars % 25
    print (quarters, "quarters")
        

    if pennies_left_quarters != 0:
        dimes = pennies_left_quarters // 10
        pennies_left_dimes = pennies_left_quarters % 10
    print (dimes, "dimes")


    if pennies_left_dimes != 0:
        nickels = pennies_left_dimes // 5
        pennies_left_total = pennies_left_dimes % 5
        print(nickels, "nickels")
        print(pennies_left_total, "pennies")
    
main()
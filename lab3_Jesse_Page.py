#Jesse Page
#Lab 3 assignment             
#This program will take prompt the user to enter their name 
# and birth month and year.
#The program will then output to the console a greeting with 
# their name, what season they were born, and whether 
# or not they were born in a leap year.
# It will also promt the user to enter an integer of
# how many pennies thay have, and print out the value
# in dollars, quarters, dimes, nickels and pennies    

def main():
    # sentinel variable
    CONTROL = "zzz"

    # Read user's name
    user_name = input("Please enter your name: ")

    # Check for the sentinal value of "zzz"
    while user_name != CONTROL:
        # call get_month function, assign return value to variable month
        month = get_month()
        # call get_year function, assign return value to variable year
        year = get_year()
        # call find_season function, assign return value to variable season
        season = find_season(month)
        # call is_leap_year function, assign return value to variable leap_year
        leap_year = is_leap_year(year)

        # Display message to the user
        if leap_year == True:
            print("Hello,", user_name, end="")
            print("! You were born in the", season, end="")
            print(".",year, "was a leap year.")
        else:
            print("Hello,", user_name, end="")
            print("! You were born in the", season, end="")
            print(".",year, "was not a leap year.")
        
        # Reads user's amount of pennies
        pennies_input = int(input("How many pennies do you have? "))
        # call penny_jar function, pass in user's amount of pennies as argument
        penny_jar(pennies_input)

        # Update read for the sentinel-controlled while loop
        # Read the next user's name or "zzz" to quit
        user_name = input("Enter your name or 'zzz' to quit: ")

def get_month():
    user_birth_month = int(input("Please enter your birth month: "))
    #input validation for birth month
    while user_birth_month <= 0 or user_birth_month > 12:
        print("Error, enter a valid birth month")
        user_birth_month = int(input("Please enter your birth month: "))
    # returns an integer from 1-12
    return user_birth_month

def get_year():
    user_birth_year = int(input("Please enter your birth year: "))
    #input validation for user_birth_year
    while user_birth_year <= 0:
        print("Error, enter a valid birth year")
        user_birth_year = int(input("Please enter your birth year: "))
    # returns an integer greater than 0
    return user_birth_year

# month parameter is the return value from function get_month 
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
    # returns a string value of the corresponding season
    return season

# year parameter is the return value from function get_year
def is_leap_year(year):
    #if-else condition to check if year is a leap year
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        # returns boolean value
        return True
    else:
        # returns boolean value
        return False

# pennies parameter is the value of the variable pennies_input
# this function will calculate and display the number of each money 
# denomination they will get when they cash them in
def penny_jar(pennies):
    try:
        #counts dollars
        dollars = pennies // 100
        #counts remaining pennies after dollars are counted
        pennies_left_dollars = pennies % 100
        print (dollars, "dollars")

        if pennies_left_dollars != 0:
            #counts quarters from remaining pennies
            quarters = pennies_left_dollars // 25
            #counts remaining pennies after quarters are counted 
            pennies_left_quarters = pennies_left_dollars % 25
        print (quarters, "quarters")
            
        if pennies_left_quarters != 0:
            #counts dimes from remaining pennies
            dimes = pennies_left_quarters // 10
            #counts remaining pennies after dimes are counted 
            pennies_left_dimes = pennies_left_quarters % 10
        print (dimes, "dimes")

        if pennies_left_dimes != 0:
            #counts nickels from remaining pennies
            nickels = pennies_left_dimes // 5
            #counts remaining pennies after nickels are counted 
            pennies_left_total = pennies_left_dimes % 5
            print(nickels, "nickels")
            print(pennies_left_total, "pennies")

    # if user does not enter a valid integer, an exception is raised
    except ValueError as err:
        print(err)
        
    
main()
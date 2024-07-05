# Author: Ashton Lee
# Github User: ashton01L
# Date: 7/5/2024

# Description: Write a program that asks the user for a (integer) number of cents,
# from 0 to 99, and outputs how many of each type of coin would represent that amount
# with the fewest total number of coins.

def calculate_change(cents):
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    cents %= 5
    pennies = cents
    return quarters, dimes, nickels, pennies

while True:
    try:
        cents = int(input("Please enter an amount in cents less than a dollar.\n"))
        if 0 <= cents <= 99:
            quarters, dimes, nickels, pennies = calculate_change(cents)
            print("Your change will be: ")
            print(f"Q: {quarters}")
            print(f"D: {dimes}")
            print(f"N: {nickels}")
            print(f"P: {pennies}")
            break
        else:
            print("Invalid input. Please enter a number between 0 and 99.\n")
    except ValueError:
        print("Invalid input. Please enter an integer. \n")

# Date : 7/11/2024
# Name:Ilyosbek
# Telegram : @valixonov04
#instagram : valixono.v_04

# Ask the user to enter an integer. Output to the console that the number entered 
# by the user is divisible by any of the numbers from 2 to 10 without a remainder.

son = input("Please . Can you enter whole numer \n >>> !")
for n in range(2,10 ,2):
    if int(son)%n == 0:
        print(f"Your number {son} to {n} at {int(son)/n}")
    elif int(son)%n != 0 :
        print(f"Your numer to {son} can not be  ")
    else:
        print("Will enter whole number !")
import os
import time
import random


def tricky():
    # Possible numbers to add
    num = [10, 20, 30, 40, 50]

    # Choose a random number from the list
    random_number = random.choice(num)

    

    # Print and speak initial instructions
    print('''IN THIS GAME YOU HAVE ONLY 10 SECONDS TO THINK.
      BEFORE THE NEXT OUTPUT COMES.''')

    # Wait for 20 seconds and clear the screen
    time.sleep(20)
    os.system("clear")

    # Print and speak instruction to think of a number
    print("Think of a number?")

    # Wait for 10 seconds and clear the screen
    time.sleep(10)
    os.system("clear")

    # Print and speak instruction to double the number
    print("Now double it.")

    # Wait for 10 seconds and clear the screen
    time.sleep(10)
    os.system("clear")

    # Print and speak instruction to add a random number
    print(f"Now add {random_number} to it from my side.")

    # Wait for 10 seconds and clear the screen
    time.sleep(10)
    os.system("clear")

    # Print and speak instruction to divide by 2
    print("Now divide It by 2.")

    # Wait for 15 seconds and clear the screen
    time.sleep(15)
    os.system("clear")

    # Print and speak instruction to subtract the original number
    print("Now subtract the number you thought of at your first.")

    # Wait for 25 seconds and clear the screen
    time.sleep(25)
    os.system("clear")

    # Determine and print the guessed number based on random_number
    if random_number == 10:
        print("5 is the answer in your mind (>_~)")

    elif random_number == 20:
        print("10 is the answer in your mind (>_+)")

    elif random_number == 30:
        print("15 is the answer in your mind (>_<)")

    elif random_number == 40:
        print("20 is the answer in your mind (>_-)")

    elif random_number == 50:
        print("25 is the answer in your mind (>_*)")

if __name__ == "__main__":
    tricky()

import random
print('Welcome to the Game!')
def roll_dice():
   return random.randint(1,6)
while True:
    input('Press enter to roll dice...')
    result = roll_dice()
    print('You rolled: ', result)
    answer = input('Do you want to roll again?(Yes/No)')
    if answer.lower() != 'yes':
        print('Thanks for playing!')
        break


'''
import random

def roll_dice():
    # Generate a random number between 1 and 6
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Simulator!")

    while True:
        input("Press Enter to roll the dice...")

        # Roll the dice
        result = roll_dice()

        print("You rolled:", result)

        # Ask if the user wants to roll again
        roll_again = input("Roll again? (yes/no): ").lower()

        if roll_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
'''


'''
import random

def roll_dice():
    return random.randint(1, 6)

print("Welcome to the Dice Rolling Simulator!")

while True:
    input("Press Enter to roll the dice...")

    result = roll_dice()

    print("You rolled:", result)

    roll_again = input("Roll again? (yes/no): ").lower()

    if roll_again != 'yes':
        print("Thanks for playing!")
        break
'''
import random
choice = ['rock', 'paper', 'scissor']
'''
def get_user_choice():
   while True:
       user_choice = input('enter your choice: ').lower()
       if user_choice in ['rock', 'paper', 'scissor']:
           return user_choice
       else:
            return "Please input 'rock', 'paper', 'scissor'"

'''
def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
   return random.choice(['rock', 'paper', 'scissor'])

def determine_winner(user_choice, computer_choice):
   if user_choice == computer_choice:
      return "It's a tie!"
   elif user_choice == 'rock' and computer_choice == 'scissor' or user_choice == 'paper' and computer_choice == 'rock' or user_choice == 'scissor' and omputer_choice == 'paper':
      return 'You win!'    
   else:
      return "Computer wins!"

if __name__ == '__main__':
   user_points = 0
   computer_points = 0
   play_again = 'yes'
   while play_again.lower() == 'yes':
      print('Welcome to the game!')
      user_choice = get_user_choice()
      computer_choice = get_computer_choice()
      print('Your choice: ', user_choice)
      print("Computer chose:", computer_choice)
      result = determine_winner(user_choice, computer_choice)
      print(result)
      if "You win" in result:
            user_points += 1
      elif "Computer wins" in result:
            computer_points += 1
      print(f"Score - You: {user_points}, Computer: {computer_points}")
      play_again = input('Play again? (yes or no): ')
   print('Thanks for playing!')
   


'''
import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissor']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors!")
    play_again = 'yes'
    while play_again.lower() == 'yes':
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("You choice:", user_choice)
        print("Computer choice:", computer_choice)
        print(determine_winner(user_choice, computer_choice))
        play_again = input("Do you want to play again? (yes/no): ")
    print("Thanks for playing!")
'''
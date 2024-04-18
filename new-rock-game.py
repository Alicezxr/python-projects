import random

def get_user_choice():
   while True:
       user_choice = input('Enter your choice: ')
       if user_choice in ['rock', 'paper', 'scissor']:
           return user_choice
       else: 
           print("Invalid input, please enter 'rock', 'paper', 'scissor'")

def get_computer_choice():
      return random.choice(['rock', 'paper', 'scissor'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
         return "It's a tie!"
    elif user_choice == 'rock' and computer_choice == 'scissor' or user_choice == 'paper' and computer_choice == 'rock' or user_choice == 'scissor' and computer_choice == 'paper':
         return 'You win!'
    else:
         return 'Computer wins!'

if __name__ == '__main__':
   print('Welcome to the Game!!!')
   user_points = 0
   computer_points =0
   play_again = 'yes'
   while play_again.lower() == 'yes':
      user_choice = get_user_choice()
      computer_choice = get_computer_choice()
      print('Your Choice: ', user_choice)
      print('Computer Choice: ', computer_choice)
      result = determine_winner(user_choice, computer_choice)
      print(result)
      if 'You win' in result:
          user_points += 1
      elif  'Computer win' in result:
          computer_points += 1
'''
      else:
          user_points += 0
          computer_points += 0
'''
      print(f"score - You: {user_points}, Computer: {computer_points}")
      play_again = input('Do you wanna play again? (Yes/No): ')
print('Thanks for Playing!')

'''
This code has a syntax error in the else statement. The else statement should not have a condition attached to it. It should be used for all other cases that are not covered by the preceding if or elif conditions. In this snippet, it seems like you're trying to apply a condition directly after else, which is not allowed in Python syntax. Therefore, this code snippet would result in a syntax error.
  
if 'You win' in result:
    user_points += 1
elif 'Computer win' in result:
    computer_points += 1
or
if 'You win' in result:
    user_points += 1
else:
    if 'Computer win' in result:
        computer_points += 1
   
'''


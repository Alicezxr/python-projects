import string 
import random
characters = string.ascii_letters + string.digits + string.punctuation
def generate_password():
   character_length = int(input('Enter the password length: '))
   password = ''.join(random.sample(characters, character_length))
   print(password)

option = input('Do you want to generate a password? (Yes/No): ')
if option == 'yes' or 'Yes':
   generate_password()
elif option == 'No':
   print('program ended!')
   quit()
else:
   print('invalid input, please input yes or no.')
   quit()


'''
import string 
import random

characters = string.ascii_letters + string.digits + string.punctuation
character_length = int(input('Enter the password length: '))
for _ in random(character_length):
     password = ''.join(random.choice(characters))
print(password)
'''



'''
password = ''
for _ in range(character_length):
    password += random.choice(characters)
print(password)
'''
'''
password = ''.join(random.choice(characters) for _ in range(character_length))
print(password)
'''


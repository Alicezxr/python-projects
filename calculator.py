def add(x, y):
   return x + y
def subtract(x, y):
   return x - y
def multiply(x, y):
   return x * y
def divide(x, y):
   if y == 0:
      return 'Error! Division by zero!'
   else:
      return x / y

print('A. Addtion')
print('B. Subtraction')
print('C. Division')
print('D. Multiplication')

while True:
   user_input = input("choose a/b/c/d: ")
   if user_input.lower() in ['a', 'b', 'c', 'd' ]:
         num1 = int(input("Enter num1: "))
         num2 = int(input("Enter num2: "))      
         if user_input.lower() == 'a':
            print('Addtion')
            print('Result:', add(num1, num2))
         elif user_input.lower() == 'b':
            print('Subtraction')
            print('Result:', subtract(num1, num2))
         elif user_input.lower() == 'c':
            print('Division')
            print('Result:', divide(num1, num2))
         elif user_input.lower() == 'd':
            print('Multiplication')
            print('Result:', multiply(num1, num2))
         next_calculation = input("Do you want to perform another calculation? (Yes/No) ")
         if next_calculation.lower() != 'yes':
           break
   else:
      print('Invalid Input, please enter a/b/c/d')



'''
while True:
   operator = input("choose 'add', 'subtract', 'divide', or 'multiply': ")
   if operator.lower() in ['add', 'subtract', 'divide', 'multiply']:
      num1 = int(input("Enter num1: "))
      num2 = int(input("Enter num2: "))
      if operator == 'add':
         print('result: ', add(num1, num2))
      elif operator == 'subtract':
         print('result: ', subtract(num1, num2))
      elif operator == 'divide':
         print('result: ', divide(num1, num2))
      elif operator == 'multiply':
         print('result: ', multiply(num1, num2))
   else:
     print("Invalid input! Enter 'add', 'subtract', 'divide', or 'multiply'") 

   next_calculation = input("Do you want to perform another calculation? (Yes/No) ")
   if next_calculation.lower() != 'yes':
      quit()
 '''


'''
def add(x, y):
    """Function to add two numbers"""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers"""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y

def divide(x, y):
    """Function to divide two numbers"""
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")

    next_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        break
'''
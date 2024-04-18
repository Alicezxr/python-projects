'''
while True:
    print('hahah')

you cannot have a return statement outside of a function in Python
A return statement is used to exit a function and optionally return a value.
If you want to continuously return 'hahah', you might want to put it inside a function and then call that function within a loop. 
'''
def get_hahah():
    return 'hahah'

while True:
    print(get_hahah())  # or do something else with the returned value

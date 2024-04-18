'''
def main():
    print(" Welcome to the email slicer ")
    print("")

    email_input = input('input your email: ')
    (username, domain1) = email_input.split('@')
    (domain, extension ) = domain1.split('.')
    print('username: ' , username)
    print('domain: ' , domain)
    print('extension: ' , extension)

while True:
    main()
'''
print(" Welcome to the email slicer ")
def email_split():
    email_input = input('input your email: ')
    username, domain1 = email_input.split('@')
    domain, extension  = domain1.split('.')
    print('username: ' , username)
    print('domain: ' , domain)
    print('extension: ' , extension)
email_split()


'''
def email_split(email):
    username, domain = email.split('@')
    domain, extension = domain.split('.')
    return username, domain, extension

def main():
    print("Welcome to the Email Slicer")
    email_input = input("Please input your email: ")
    username, domain, extension = email_split(email_input)
    print("Username:", username)
    print("Domain:", domain)
    print("Extension:", extension)

if __name__ == "__main__":
    main()
'''
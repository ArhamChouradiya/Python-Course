"""    ONE WAY TO ASSERT
num=int(input("ENTER EVEN NUMBER:"))
assert num%2==0,"YOU HAVE ENTERED ODD NUMBER"
"""
"""

try:
    
    num=int(input("ENTER EVEN NUMBER:"))
    assert num%2==0
except AssertionError:
    print("YOU HAVE ENTERED ODD NUMBER")    
    
print("AFTER THE ASSERTION")

"""


class InvalidPasswordException(Exception):
    pass

while True:
    try:
        password = input('Enter your password: ')
        if len(password) < 8:
            raise InvalidPasswordException

    except InvalidPasswordException:
        print()
        print('ERROR: Password length under 8 characters')
        print()
    else:
        print('Valid Password')
        break
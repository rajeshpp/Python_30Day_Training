class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter Age: "))
    if age<0:
        raise InvalidAgeError
    
except InvalidAgeError:
    print("Invalid Age given")

#TWO.py

def func():
    print("THE FUNCTION in ONE.py")

print("Top level in ONE.py")

if __name__ == '__main__':
    print("The ONE.py is being executed directly!")
else:
    print("THE ONE.py has been only imported!")

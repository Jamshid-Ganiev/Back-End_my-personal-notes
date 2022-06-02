
import ONE
def func2():
    print("Im the FUNCT2 in TWO.py file")
print("TOP level in TWO.py")
ONE.func()
if __name__ == '__main__':
    print("THE TWO.py is being executed directly!")
else:
    print("TWO.py has only been imported! to another module")

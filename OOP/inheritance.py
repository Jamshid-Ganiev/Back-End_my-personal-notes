class Animal():

    def __init__(self):
        print("Animal Created!")

    def who_am_i(self):
        print("I am an Animal")

    def eat(self):
        print("I am eating")

#Inheritance
#Inheritance is a way to form new classes using classes that have already been defined.
#The newly formed classes are called derived classes, the classes that we derive from are called base classes.
# Important benefits of inheritance are code reuse and reduction of complexity of a program.
# The derived classes (descendants) override or extend the functionality of base classes (ancestors).

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        ##Inheriting the old class to the new one so that we can access all functions from old one in new one

        print("Dog Created")
    def bark(self):
        print("Woof!")

## operations on them
my_dog = Dog()

my_dog.bark()

#////////OPTIONAL////// NOT COMMONLY USED UNTIL MUCH LATER IN YOUR pYTHON CAREER:)
#******Polymorphism***********
#In Python, polymorphism refers to the way in which different object classes can share the same method name,
# and those methods can be called from the same place even though a variety of different objects might be passed in.
class Dog():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' says Woof! Woof!'

class Cat():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name +' says Meow! Meow!'
#inputs
chapa = Dog('chapa')
baroq = Cat('baroq')

a = chapa.speak()
print(a)
b = baroq.speak()
print(b)

#Here we have a Dog class and a Cat class, and each has a .speak() method.
#When called, each object's .speak() method returns a result unique to the object.
######There a few different ways to demonstrate polymorphism. First, with a for loop:
# with for loop
for pet in[chapa,baroq]:
    print(pet.speak())


#another with functions:
def pet_speak(pet):
    print(pet.speak())
pet_speak(baroq)
pet_speak(chapa)

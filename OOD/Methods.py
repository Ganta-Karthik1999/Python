class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def welcome(self):
        print(f"My name is {self.name}")

    def get_info(self):
        return f"{self.name} age is {self.age}"    

    # Methods Modifying the Properties
    def celebrate_birthday(self):
        self.age=self.age+1
        print(f"My age after the birthday is {self.age}")

    def __str__(self):
        return f"The name is {self.name} and age is {self.age}"

# Here we will learn about the method with parameters
class calculator:
    def add(self,a,b):
        return f"The addition of two number's is {a+b}"

    def multiply(self,a,b):
        return f"The multiplication of two number's {a*b}"

# The __str__() method is a special method that controls what is returned when the object is printed:
# __str__() ==> this will send the return value once we call the object


if __name__ == '__main__':
    p1=Person("Karthik",25)
    p1.welcome()

    p2=calculator()
    print(p2.add(2,3))
    print(p2.multiply(2,3))

    # Method Accessing Properties
    print(p1.get_info())

    p1.celebrate_birthday()

    print(p1)
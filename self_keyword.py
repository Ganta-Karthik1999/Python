class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        return "Hello " + self.name

    def welcome(self):
        print(self.greet() + "welcome to our website !!")


if __name__ == '__main__':
    p1=Person("Karthik ",25)
    p1.welcome()
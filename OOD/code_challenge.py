class Person:
    def __init__(self,name,age):
        self.name =name
        self.age=age

    def greet(self):
        print("Hello,my name is "+ self.name)


if __name__ == '__main__':
    p1=Person("John",36)

    print(p1.name)
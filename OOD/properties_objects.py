class Person:
    # class properties
    # this is shared betwwen all the object
    company = "J&J"
    team =""

    def __init__(self,name,age):
        # Instance Properties
        # this is local to each object
        self.name=name
        self.age =age

Person.team = "software"

if __name__ == '__main__':
    p1=Person("Karthik",25)

    # Accessing the properties
    print(p1.name)
    print(p1.age)
    print("=========================")

    # Modifying the properties
    p1.age = 26
    print(p1.age)
    print("========================")

    p3=Person("yo bro",23)
    print(p3.company)
    print("======================")

    print(p3.team)

    # Delete the Properties
    del p1.age

    # Adding new Properties
    p3.role="Developer"

    print("======================")
    print(p3.role)




    
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def printname(self):
        print(self.fname,self.lname)

class Students(Person):
    pass

if __name__ == '__main__':
    p1 = Students("karthik","Ganta")
    p1.printname()
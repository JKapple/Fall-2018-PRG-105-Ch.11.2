#import ProductionWorker

class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber


class ProductionWorker(Employee):
    def __init___(self,shift,wage):
        self.shiftNumber = shift
        self.hourlyWage = wage



x = Person("Jack", "Black")
y = Employee("Ben", "Kapple", "1007")

print(x.Name())
print(y.GetEmployee())

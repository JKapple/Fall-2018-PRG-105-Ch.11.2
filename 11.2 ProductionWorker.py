#import Employee

usrFName = input("Enter your first name: ")
usrLName = input("Enter your last name: ")
usrShift = input("Enter your shift number: ")
usrWage = input("Enter your hourly pay rate: ")




if usrShift == "1" :
    usrShift = "Day"
else:
    usrShift = "Night"

#usrFName,usrLName,usrShift,usrWage

#class ProductionWorker(Employee):
 #   def __init___(self,shift,wage):
  #      self.shiftNumber = shift
   #     self.hourlyWage = wage
    #def get_shift(self):
     #   return
#shift = input("Your shift is " + shiftNumber)
#shift = input("Your shift is " + shiftNumber)
#return "your shift is" + self.shiftNumber + "/n your wage is "

print ("Your First name is " + usrFName + "\n Your Last Name is " + usrLName  + "\n Your Shift is " + usrShift  + "\n Your hourly pay rate is " + usrWage)

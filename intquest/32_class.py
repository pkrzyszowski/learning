class Person():
#method
    def inputName(self,fname,lname):
        self.fname=fname
        self.lname=lname
    #method
    def showFullName(self):
        print(self.fname +" "+ self.lname)

person1 = Person()
person1.inputName('Piotrtttt', 'Krzyszowski')
person1.showFullName()

#object instantiation person1.inputName("Ratan","Tata") #calling a method inputName person1. showFullName() #calling a method showFullName()
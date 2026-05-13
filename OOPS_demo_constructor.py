# self keyword is mandatory for callling variable names into method
# instance and class variable have whole different meaning and usage
# costructor name should be __init__

class calculator:
    num=100 #class variable
    # default constructor

    def __init__(self ,a,b):
        self.firstnumber =a
        self.secondnumber =b
        print("I am executing as constructor")

    def getdata(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstnumber + self.secondnumber + self.num

obj = calculator(2,3)
obj.getdata()
print(obj.Summation())


obj1= calculator(4, 5)
obj1.getdata()
print(obj1.Summation())

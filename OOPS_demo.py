class calculator:
    num=100

    def getdata(self):
        print("I am now executing as method in class")

obj = calculator()
obj.getdata()
print(obj.num)
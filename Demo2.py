# variables print and adding values in list
# list is data type that allow multiple values and can be different data types



values = [1,2,"Rahul",4,5,]
print(values)

print(values[0])  # Output: 1
print(values[1])    # Output: 2
print(values[2])   # Output: "Rahul"
print(values[3])  # Output: 4
print(values[4])  # Output: 5


# print the range of values in list
print(values[1:3])  # Output: [2, "Rahul"]

# for adding values in list we can use append() method or insert() method
values.insert(3,"sid")
print(values)
values.insert(4,"dixit")
print(values)
values.insert(0,"hello")
print(values)
values.insert(0,"DIXIT")
print(values)
values.append("welcome")
print(values)
#                delete values in a list of variable
del values[4]
print (values)
#               delete multiple values in a list of variable
del values[0:1]
print (values)
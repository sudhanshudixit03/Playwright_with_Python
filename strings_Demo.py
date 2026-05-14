str = "SudhanshuDixit.com"
str1 = "Consulting firm"
str3 = "Arun"


print(str[1])                                 #output will be "u" as index starts with 0 in python


print(str[0:5])                                #if you want substring in python output will be "Sudha" as index starts with 0 and it will print till 4th index


print(str + str1)                            #concatenation- output will be "SudhanshuDixitConsulting firm"


print(str3 in str)                           # checking if str3 is present in str or not if yes output will TRUE if not then output will be FALSE

#split method is used to split the string based on the separator provided in this case it is "."

var = str.split(".")
print (var)                                  #output will be ['SudhanshuDixit', 'com'] as split method will split the string based on
                                            # the separator provided in this case it is "."

print(var[0])                                 #output will be "SudhanshuDixit" as it is the first element in the list created by split method

#Trim method is used to remove the leading and trailing spaces from the string
str4= " great"
print(str4.strip())           #output will be "great" as strip method will remove the leading and trailing spaces from the string


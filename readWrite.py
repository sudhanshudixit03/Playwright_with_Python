file = open('test.txt')
                                #read all the contents of the file


# print(file.read())


                                #read one single line at a time


# print(file.readline())
# print(file.readline())




                                # print line by line using readline method
                                # using 'for loop' to read line by line
#values= [abc,bvvdsf,cat,dog,elephant]
for line in file.readlines():
    print(line)


file.close()
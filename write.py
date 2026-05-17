                    # another way to open a txt file

# with open ('test.txt') as file:


                    # if we want to read the file we should use 'r'

with open ('test.txt', 'r') as reader:          #using reader as object because i am reading this file
    content = reader.readlines()       #readlines() is used to read the file line by line ,output =[abc,bvvdsf,cat,dog,elephant]
    reversed(content)                   #output will be in reversed list =[elephant,dog,cat,bvvdsf,abc]



           # and if we want to write the file we should use 'w'


with open ('test.txt','w') as writer:          #using writer as object because i am writing this file
    for line in reversed(content):                   #using for loop to write the reversed content in the file
        writer.write(line)                #this will write the reversed content in the file
                                        #output will be in reversed list =[elephant,dog,cat,bvvdsf,abc]
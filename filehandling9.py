file = open("C:\\Users\\jaspr\\OneDrive\\Desktop\\python in vs code\\abc.txt",'a')
 
with open("abc.txt",'r') as myfile:
    data = myfile.readlines()

data_2 = data[::-1]
""" Now we will just write the fully reverse
    list in the output2 file using following command """
f2.writelines(data_2)

f2.close()    
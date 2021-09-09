file = open("C:\\Users\\jaspr\\OneDrive\\Desktop\\python in vs code\\abc.txt",'a')

with open("C:\\Users\\jaspr\\OneDrive\\Desktop\\python in vs code\\abc.txt",'r') as myfile:
    data = myfile.readlines()

data_1 = data[::-1]

file.writelines(data_1)

file.close()
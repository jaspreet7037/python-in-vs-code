""" In this Python program the content in the file will get 
    stored in another file in reverse order . """  

file = open("C:\\Users\\jaspr\\OneDrive\\Desktop\\python in vs code\\abc.txt",'a')

with open("C:\\Users\\jaspr\\OneDrive\\Desktop\\python in vs code\\abc.txt",'r') as myfile:
    data = myfile.read()  
    
data_1 = data[::-1]

file.write(data_1)

file.close()
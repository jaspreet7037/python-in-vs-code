file = open("C:\\Users\\jaspr\\OneDrive\\Desktop\\python in vs code\\abc.txt",'a')
str = input("Enter the text to send it to the file = ")
st = file.write(str)
print("The statemwnt contains",st,"character")
file.write("\n")
file.close()
# wap which input 5 records in a file mmm.csv .

import csv

file = open("C:\\Users\\jaspr\\OneDrive\\Desktop\\python in vs code\\mmm.csv",'a')
wr = csv.writer(file)
n = int(input('ENTER THE LIMIT : '))
for i in range(1,n+1,1):
    print("Enter the record:",i)
    rollno = int(input('enter rollno:')) 
    name = input("enter name:")
    marks = int(input('enter the marks:'))
    wr.writerow([rollno,name,marks])
file.close()


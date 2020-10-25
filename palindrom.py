no = int(input("enter the number"))
rev = 0
temp = no
while no!=0:
    rem=no%10
    rev=rev*10+rem
    no=no//10
if rev==temp: 
     print('number is palindrom')
else:
    print('number is palindrom')



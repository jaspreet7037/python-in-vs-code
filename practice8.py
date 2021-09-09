def greaterthree(a,b,c):
    if a>=b and a>=c:
        print(a,"is greater than ",b," and ",c)
    if b>=a and b<=c:
        print(b,"is greater than ",c," and ",a)
    else:
        print(c,"is greater than ",a," and ",b,)

i = int(input("Enter the first number = "))
j = int(input("Enter the second number = "))
k = int(input("Enter the third number = "))
greaterthree(i,j,k)
         
    

def greater(a,b):
    if a>b:    
        print("This number",a,"is bigger than",b)
    else:
        print("This number",a,"is smaller than",b)
    return 0;

f = int(input("Enter The Number : "))
g = int(input("Enter The Number : "))
greater(f,g)
def palindrome(no):
    rev=0
    temp=0
    while no!=0:
        rev=no%10
        rev=rev*10+rev
        no=no//10
    if rev==temp: 
        print("This number is palindrome")
    else: 
        print("This number is not palindrome number")    
        
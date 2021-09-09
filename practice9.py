# In this program you can check whether the character is in uppercase or lowercase or non alphabetic character 

def upper(ch):
    if ch>='A' and ch<='Z':
        print(ch,"is an UpperCase character")

    elif ch>='a' and ch<='z': 
        print(ch,"is an lowerCase character")
    else: 
        print(ch,"is not an alphabetic character")

# Driver Code 

# Get the character
ch = 'A'

# check the character
upper(ch)

# Get the character
ch = 'a'

# check the character
upper(ch)

# get the character
ch = '0'

# check the character
upper(ch)


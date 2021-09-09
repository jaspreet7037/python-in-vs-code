def consonant(ch):
    if ch!='A' or ch!='E' or ch!='I' or ch!='O' or ch!='U' or ch!='a' or ch!='e' or ch!='i' or ch!='o' or ch!='u':
        print(ch," is a consonant")
    else:
        print(ch," is a vowel")

character = str(input("Enter the character to check if it is a consonant or not : "))
consonant(character)
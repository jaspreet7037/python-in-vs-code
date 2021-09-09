def vowel(ch):
    if ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U' or ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        print(ch," is a vowel.")
    else:
        print(ch," is a consonant.") 

character = str(input("Enter the character to check if it is vowel or not : "))
vowel(character)
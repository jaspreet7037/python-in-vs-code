def encrypt(sttr,enkey):
    return enkey.join(sttr)
def decrypt(sttr,enkey):
    return enkey.split(sttr)

# __main__
mainString = input("Enter the main string : ")   
encryptStr = input("Enter the encryption key : ")
enStr = encrypt(mainString, encryptStr)
delst = decrypt(enStr,encryptStr)
destr ="".join(delst)
print("The encrypted String is : ",enStr)
print("String after decryption is : ",destr)

import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&amp;*1234567890"
lenght = int(input("Enter Password lenght  "))
password = ""
 
for i in range(lenght+1):
    password += random.choice(characters)
print(password)




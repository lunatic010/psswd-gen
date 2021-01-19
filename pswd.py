import random

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

l1=chr(random.randint(65,90))
l2=chr(random.randint(35,60))
l3=chr(random.randint(45,100))
l4=chr(random.randint(65,90))
l5=chr(random.randint(65,70))
l6=chr(random.randint(45,90))
l7=chr(random.randint(45,60))
l8=chr(random.randint(45,90))
l9=chr(random.randint(65,90))
l10=chr(random.randint(75,90))
l11=chr(random.randint(45,90))
l12=chr(random.randint(65,90))
password = l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 + l10 + l11 + l12
password = shuffle(password)

print(password)

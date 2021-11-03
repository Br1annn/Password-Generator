import random
import string

#length of password
leng = int(input('Enter Password Length: '))

#define ascii values

lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
symbols = string.punctuation
numbers = string.digits

#combine data

password = upperCase + lowerCase + symbols + numbers

#output length randomly

empty = random.sample(password,leng)

#combine random code

newPassword = ''.join(empty)

#print password

print(newPassword)


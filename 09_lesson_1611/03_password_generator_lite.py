import random as r
import string

length = int(input('Сколько символов нужно? '))
raw_pass = string.ascii_letters + string.digits + string.punctuation
password = ''

for i in range(length):
    password += r.choice(raw_pass)

print(password)

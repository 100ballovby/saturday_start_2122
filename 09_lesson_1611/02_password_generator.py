import random as r
import string

length = int(input('Сколько символов нужно? '))
raw_pass = string.ascii_letters
digits = input('Нужны ли числа? (+/-) ')
symbols = input('Нужны ли спец.символы? (+/-) ')
dig_p = string.digits  # цифры
dig_o = string.punctuation  # спец.символы

if digits == '+' and symbols == '+':
    raw_pass += (dig_o + dig_p)
elif digits == '+':
    raw_pass += dig_p
elif symbols == '+':
    raw_pass += dig_o

password = ''

for i in range(length):
    password += r.choice(raw_pass)

print(password)



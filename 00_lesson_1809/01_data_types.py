x = 8
y = '5'
z = 8.42
a = '2.36'
b = 'one'

# print(int(b))  -> ValueError
print(int(y))
print(int(z))
# print(int(a))  -> ValueError
print(int(float(a)))
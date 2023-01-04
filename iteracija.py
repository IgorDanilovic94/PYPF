string = "3,9,13,4,42"
b = (string.split(','))
print(b)
#print(type(b))
c = [int(i) for i in b]
print(c)
#print(type(c))
d = [(i**2) for i in c]
print(d)
#print(type(d))
e = str(d)
print(e)
#print(type(e))
print(e[1:-1])

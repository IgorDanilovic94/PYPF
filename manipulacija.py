a = 4
b = 1
c = 9
d = 3
with open('izrazi.txt','w') as f:
    f.write(str(int(a)) + '-' + str(int(b)) + '\n')
    f.write(str(int(c)) + '-' + str(int(d)))

with open ('./izrazi.txt', 'r') as f1:
    print(f1.readline())
    print(f1.readline())

with open('izlaz.txt','w') as f2:
    f2.write(str(a)+'-'+str(b)+'='+str(a-b) + '\n')
    f2.write(str(c)+'-'+str(d)+'='+str(c-d))

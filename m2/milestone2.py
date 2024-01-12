import re 
file = open('m2\Testcase1.txt', 'r')
a=file.readlines()
b=[]
for line in a:
    words = re.split(':|\| ', line)
    a=words[1]
    b.append(a)
s1 = slice(3)
d=int(b[0])
s=(b[1])
dsv=(b[2])
r=(b[3])
s=s.split('x')
s=int(s[0])
print(d)
print(s)
print(dsv)
print(r)

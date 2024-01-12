import re
import math
import numpy
file = open('Testcase2.txt', 'r')
a=file.readlines()
b=[]
for line in a:
    words = re.split(':|\| ', line)
    a=words[1]
    b.append(a)
s1 = slice(3)
d=int(b[0])
n=int(b[1])
a=int(b[2])
print(d,n,a)
def slope(x1, y1, x2, y2):
  s = (y2-y1)/(x2-x1)
  return s
r=d/2
an=math.radians(a)
x1 = r*math.cos(an)
y1 = r*math.sin(an)

x2=-1*x1
y2=-1*y1
print(x1,y1)
print(x2,y2)
p1=[]
p2=[]
p1.append(x1)
p1.append(y1)
p2.append(x2)
p2.append(y2)
def getEquidistantPoints(p1, p2, parts):
    return zip(numpy.linspace(p1[0], p2[0], parts),
               numpy.linspace(p1[1], p2[1], parts))
sol=list(getEquidistantPoints((x1,y1), (x2,y2), n))
ans=open('output2.txt', 'w')
for i in sol:
    ans.write(str(i)+'\n')







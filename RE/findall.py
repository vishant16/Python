import re

a="vishAnt is $2329832  0  11 asdhasd,./. -11 -12 -1212"

#p.findall()
a1=re.compile('\d')
b1=a1.findall(a)
print("Numerical data: ",b1)

a2=re.compile('\d+')
b2=a2.findall(a)
print("Numerical data>(1-9): ",b2)

a3=re.compile('\W')
b3=a3.findall(a)
print("Without Alphanum: ",b3)

a4=re.compile('\w')
b4=a4.findall(a)
print("Without Alphanum: ",b4)

a5=re.compile('\s')
b5=a5.findall(a)
print("Whitespace character: ",b5)

a6=re.compile('\S')
b6=a6.findall(a)
print("Non Whitespace character: ",b6)

a7=re.compile('\D')
b7=a7.findall(a)
print("Non Digit character: ",b7)


#p.split()
#p.sub()
#p.subn()
#p.escape()




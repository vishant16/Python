""" unpacking sequence/iterable into variables """

a=(1,2,3)#/list/string
x,y,z=a
print(x,y,z)

""" discarding values"""
b=[1,2,'string1',4,'string2']
x,y,_,z,_=b
print(x,y,z)

"""  * variable """
b=[1,2,3,4,5,6]
x,y,*z=b
print(x,y,z)

""" dicarding multiple values"""
x,y,*_=b
print(x,y)

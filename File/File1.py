""" printing whole file contents

alternate
file=open('file.txt',r/w/a/r+)
r=read,
w=write
a=append
r+=r+w
"""
import os
file=open('OK.txt','w')
     #content=file.readline() #print only one line
     #content=file.readlines() #chnages to list
    #content=file.read(20)  # 20-n characters from files
     #file.write(" written")
     #file.close()
#print(content)
print(file.tell())
#os.rename('file_Ok.txt','file_OkK.txt')

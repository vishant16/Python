file=open("file.txt",'r+')
#file.write("new line is added")
#print(file.readline()) # return one line
#print(file.read()) #return whole content
#print(file.readable()) # Return T/F
#print(file.writable())  # Return T/F
#file.seek(15) # set current file position to 10 index
#print(file.readlines()) # return file in list
#print(file.seekable())
#print(file.tell()) # return current file position index
#file.truncate(10) # rezie the file according to given bytes
#file.writelines(["first","second"]) # right items in file in list format
print(file.isatty())
print(file.readlines())
file.close()

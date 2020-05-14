"""
file to list
we can apply list methods on j
"""

with open('New2_file.txt','w') as file: # or file=open('file.txt',r/w/a/r+)
    content=file.readlines() #chnages to lis
    # cotnent=file.readline()
    x=file.write("New file created")
    x.close()

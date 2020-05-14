class parent:

    def __new__(self):
        print("parent_new")
    def __init__(self):
        print("parent_init")

class child(parent):
    def __new__(self):
        print("child_new")
    def __init__(self):
        print("child_init")

a=parent()
print(a)

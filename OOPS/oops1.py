class parent:
    def __init__(self):
        print("parent")
class child(parent):
    child.__init__(self)

a=child()

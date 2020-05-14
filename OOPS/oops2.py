class A:
     def __init__(self):
         self.i = 1
         self.j = 5

     def display(self):
         print(self._i, self._j)
class B(A):
     def __init__(self):
         super().__init__()
         self._i = 3
         self.j = 7
c = B()
c.display()

class A(object):
    def foo(self):
        print('A.foo()')

class B(object):
    def foo(self):
        print('B.foo()')

class C(B, A):
    pass

c = C()
c.foo()

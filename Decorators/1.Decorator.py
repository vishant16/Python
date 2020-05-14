"""
Decorators
1. It is tool which changes function behavior without permanently modifing that function.
2. function as argument and return function
"""

#defining Decorators
def decorator(func):
    #wrapper function
    def wrapper():
        print("I am wrapper function")
        func()
    return wrapper


# this is Syntactic Sugar!
@ decorator
#function used in wrapper
def used():
    print("function used in wrapper function")

# passing used in decorator
# @decorator or we can use used=decorator(used)
used()

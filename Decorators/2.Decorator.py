
def decorator(func):

    def wrapper(*args,**kwargs):
        x=func(*args,**kwargs)
        return x
    return wrapper


@decorator
def sum(a,b):
    return a+b

print(sum(1,2))

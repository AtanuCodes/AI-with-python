from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print('Before Function')
        func()
        print('After function')
    return wrapper

@my_decorator
def greet():
    print('Hello!')

greet()
# print(greet.__name__)
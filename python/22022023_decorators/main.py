"""

decorators
"""
def printtt(n):
    def print_(func):
        def wp(*args, **kwargs):
            print("Hello", n)
            f = func()
            return f

        return wp
    return print_

@printtt(10)
def hello():
    print('Hello Sir!')


def multiply(n):
    def print_(func):
        def wp(*args, **kwargs):
            f = func()*n
            return f
        return wp
    return print_


@multiply(5)
def mult(n):
    return n**2





import sympy

def definite_integral(f, a, b):
    x = sympy.Symbol('x')
    return sympy.integrate(f, (x, a, b))

# Example
f = sympy.sin(x)
a = 0
b = sympy.pi

print(definite_integral(f, a, b))
# 2


import sympy

def integrate(f, var):
    return sympy.integrate(f, var)

#Example
x = sympy.Symbol('x')
f = x**2

integrate(f, x)
#Output: x**3/3
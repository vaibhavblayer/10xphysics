

import sympy

def derivative(f, var):
    x = sympy.Symbol(var)
    return sympy.diff(f, x)

#Example
f = x**2 + 3*x + 1
derivative(f, 'x')
# Output: 2*x + 3
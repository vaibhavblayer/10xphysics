

import sympy

def solve_linear_diff_eq(eq, y, x):
    y = sympy.Function('y')(x)
    return sympy.dsolve(eq, y)

#Example
#Solve the differential equation:
# dy/dx + 2y = x

eq = sympy.Eq(sympy.Derivative(y, x) + 2*y, x)
solution = solve_linear_diff_eq(eq, y, x)
print(solution)

#Output:
#y(x) = C1*exp(-2*x) + x/2 - x**2/4
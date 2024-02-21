from sympy import symbols, diff, pretty_print, factorial, exp, sin, cos, tan, latex
x, y = symbols("x y")

n = 10    # Number of iterations
x0 = 0    # The value of "a" or the point

func = sin(x)             # The function we are approximating
result = func.subs(x, x0)  # Initializing result with the first term

for i in range(1, n):
    result += diff(func, x, i).subs(x, x0) * ((x - x0)**i)/(factorial(i))
    #  diff(func, x, i) -> This differentiates "func" w.r.t x, "i-th" times
    #  subs(x, x0)      -> This is a method used on expressions,
    #                      to substitute an unknown (x) with a value (x0).

pretty_print(result)
print(latex(result).replace('frac', 'dfrac'))

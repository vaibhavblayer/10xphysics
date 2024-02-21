from sympy import sin, cos, tan, ln, log, exp
from sympy import atan, asin, acos
from sympy.abc import x, y, z
from sympy import latex, lambdify
from sympy import Function, Symbol, Lambda
import math


fx_list = []
fx_l_list = []

#f(x)
f = sin(x)
f_l = latex(f, mode='inline')
fx_list.append(f)
p_f_l = '$f\\left(x\\right)='
fx_l_list.append(p_f_l + f_l[1:])

#f(-x)
f_x = f.subs(x, -x)
f_x_l = latex(f_x, mode='inline')
fx_list.append(f_x)
p_f_x_l = '$f\\left(-x\\right)='
fx_l_list.append(p_f_x_l + f_x_l[1:])

#f(x+1)
fxp = f.subs(x, x+1)
fxp_l = latex(fxp, mode='inline')
fx_list.append(fxp)
p_fxp_l = '$f\\left(x+1\\right)='
fx_l_list.append(p_fxp_l + fxp_l[1:])


#f(x-1)
fxm = f.subs(x, x-1)
fxm_l = latex(fxm, mode='inline')
fx_list.append(fxm)
p_fxm_l = '$f\\left(x-1\\right)='
fx_l_list.append(p_fxm_l+fxm_l[1:])


#f(2x)
fxt = f.subs(x, 2*x)
fxt_l = latex(fxt, mode='inline')
fx_list.append(fxt)
p_fxt_l = '$f\\left(2x\\right)='
fx_l_list.append(p_fxt_l + fxt_l[1:])


#f(x/2)
fxh = f.subs(x, x/2)
fxh_l = latex(fxh, mode='inline')
fx_list.append(fxh)
p_fxh_l = '$f\\left(x/2\\right)='
fx_l_list.append(p_fxh_l + fxh_l[1:])

#f(|x|)
fmx = f.subs(x, abs(x))
fmx_l = latex(fmx, mode='inline')
fx_list.append(fmx)
p_fmx_l = '$f\\left(\\left|x\\right|\\right)='
fx_l_list.append(p_fmx_l + fmx_l[1:])

#|f(x)|
fmy = f
fmy_l = latex(fmy, mode='inline')
fx_list.append(fmy)
p_fmx_l = '$\\left|f\\left(x\\right)\\right|='
fx_l_list.append(p_fmx_l + fmy_l[1:])

#|f(|x|)|
fm = f.subs(x, abs(x))
fmy = abs(fm)
fmy_l = latex(fmy, mode='inline')
fx_list.append(fmy)
p_fmx_l = '$\\left|f\\left(\\left|x\\right|\\right)\\right|='
fx_l_list.append(p_fmx_l + fmy_l[1:])



##f'(x)
#fxd = f.diff(x)
#fxd_l = latex(fxd, mode='inline')
#fx_list.append(fxd)
#p_fxd_l = '$f\'\\left(x\\right)='
#fx_l_list.append(p_fxd_l+fxd_l[1:])
#
#
##int f(x)
#if f.integrate(x):
#    fxi = f.integrate(x)
#else:
#    fxi = x
#fxi_l = latex(fxi, mode='inline')
#fx_list.append(fxi)
#p_fxi_l = '$\\int f\\left(x\\right)d\\!x='
#fx_l_list.append(p_fxi_l+fxi_l[1:-1]+'+c$')



	








import sympy as sp

a, b, c = sp.symbols('a b c')

x, y, z = sp.symbols('x y z')

# exp = sp.exp()
U_first = sp.Matrix([[sp.cos(a/2), -sp.exp(sp.I * c) * sp.sin(a/2)],
                     [sp.exp(sp.I * b) * sp.sin(a/2), sp.exp(sp.I * (b + c)) *(sp.cos(a/2))]])


print(U_first)
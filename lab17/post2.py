import sympy as sp
# Define symbols
z, omega = sp.symbols('z omega')
X_z = z * (z - sp.cos(omega)) / (z**2 - 2*z*sp.cos(omega) + 1)
print("Z-transform of x[n] = cos(ω n) u[n]:")
sp.pprint(X_z, use_unicode=True)

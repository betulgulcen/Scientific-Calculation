# Gauss-Seidel Yöntemi örneği
# 9x+3y+z=13 -6x+8z=2 2x+5y-z=6
# Her denklemde 1 bilinmeyen yalnız bırakılır.

y,z= 0,0
for i in range(100):
    x=(13-3*y-z)/9
    y=(6+z-2*x)/5
    z=(2+6*x)/8
print(x,y,z)

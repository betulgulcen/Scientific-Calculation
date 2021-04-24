# Jacobi İterasyonu Yöntemi örneği
# 9x+3y+z=13 -6x+8z=2 2x+5y-z=6
# Her denklemde 1 bilinmeyen yalnız bırakılır. Gauss'tan farkı her bilinmeyene değer verilmesi ve tamamen baştan hesaplanmasıdır. (x'i kullanmadan)

x,y,z=0,0,0
for i in range(100):
    x,y,z=(13-3*y-z)/9,(6+z-2*x)/5,(2+6*x)/8
print(x,y,z)

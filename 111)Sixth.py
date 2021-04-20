# Sekant yöntemi ile iki bilinmeyenli denklem

# f(x,y)=x**2-2*x-8=0 çözelim.

def f(x):
    return(x**2-2*x-8)
x1= float(input("başlangıç tahmini girin: "))
x3= float(input("başlangıç tahmini girin: "))

while(f(x3)!=f(x1)):
    x2 = x1- (f(x1)*(x3-x1))/(f(x3)-f(x1))
    print(x3)
    x1, x3 = x3, x2

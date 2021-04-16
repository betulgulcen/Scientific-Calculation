# Newton-Ralph Yöntemi 

#(x**2-3x-4 için)
def f(x):
  return(x**2-3*x-4)

def fi(x):
    return(2*x-3)
def hata(x1,x2):
    return(abs((x1-x2)/x1))
x1 = int(input("tahmin girin: "))

for i in range(10):
    x2=x1-f(x1)/fi(x1)
    print(x1,x2,hata(x1,x2))
    x1=x2
    

#(e**(-2x)-x için)
from math import e

def f(x):
  return(e**(-2*x)-x)

def fi(x):
    return(-2*e**(-2*x)-1)
def hata(x1,x2):
    return(abs((x1-x2)/x1))
x1 = int(input("tahmin girin: "))

for i in range(10):
    x2=x1-f(x1)/fi(x1)
    print(x1,x2,hata(x1,x2))
    x1=x2
    
    
#(x**(-10)-1 için)

def f(x):
  return(x**10-1)

def fi(x):
    return(10*x**9)
def hata(x1,x2):
    return(abs((x1-x2)/x1))

x1 = int(input("tahmin girin: "))
h=1

while(h>(10**(-10))):
    x2 = x1 - f(x1)/fi(x1)
    h= hata(x1,x2)
    print(x1,h)
    x1=x2

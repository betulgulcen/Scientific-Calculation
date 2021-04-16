#f(x)=x**2-3x-4 fonksiyonunun köklerini tahminler üzerinden bulan python kodu

def f(x):
  return(x**2-3*x-4)
x1=int(input("ilk tahmin: "))
x2=int(input("ikinci tahmin: "))

if(f(x1)*f(x2)==0):
  print("tahminlerinizden biri köktür")
elif(f(x1)*f(x2)>0):
  print("bu aralıkta kök yoktur")
else:
  for i in range(10):
    xr=(x1+x2)/2
    if(f(xr)==0):
      print("denklemin kökü:", xr)
      break
    elif(f(x1)*f(x2)<0):
      x2=xr
    else:
      x1=xr
    print(xr, i)

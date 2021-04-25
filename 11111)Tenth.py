#Verilerin doğruya yaklaştırılması

xi=[1,2,3,4,5,6,7]
yi=[0.5,2.5,2,4,3.5,6,5.5]
n=len(xi)

xiyi,xi2=0,0
for i in range(n):
    xiyi += xi[i]*yi[i]
    xi2 += xi[i]**2

a1= (n*xiyi-sum(xi)*sum(yi))/(n*xi2-sum(xi)**2)
a0= sum(yi)/n-a1*sum(xi)/n

# Standart Sapma hesabı
standartsapma=0
for i in range(n):
    standartsapma += (yi[i]-sum(yi)/n)**2

standartsapma = (standartsapma/(n-1))**(1/2)

# Ortalama Hata Hesabı
orthata=0
for i in range(n):
    y=a0+a1*xi[i]
    orthata += yi[i]-y
orthata= (orthata/(n-2))**(1/2)

print(a0,a1,standartsapma,orthata)

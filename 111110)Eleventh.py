# 10 günlük Covid-19 ölüm verilerinden, 11. gün ölüm sayısı tahmini

xi=[1,2,3,4,5,6,7,8,9,10]
yi=[211,276,258,253,248,237,243,273,279,297]
n=len(xi)

xiyi,xi2=0,0
for i in range(n):
    xiyi += xi[i]*yi[i]
    xi2 += xi[i]**2

a1= (n*xiyi-sum(xi)*sum(yi))/(n*xi2-sum(xi)**2)
a0= sum(yi)/n-a1*sum(xi)/n

standartsapma=0
for i in range(n):
    standartsapma += (yi[i]-sum(yi)/n)**2
standartsapma = (standartsapma/(n-1))**(1/2)

orthata=0
for i in range(n):
    y=a0+a1*xi[i]
    orthata += yi[i]-y
orthata= abs((orthata/(n-2)))**(1/2)

print(a0+a1*11)

import numpy as np
import matplotlib.pyplot as plt

'''a = float(input("coefficient en X²: "))
b = float(input("coefficient en X: "))
c = float(input("coefficient constant: "))
x = np.linspace(-10, 10, 100)

f = a*x**2 + b*x + c
D = b**2 -4*a*c
if D > 0:
    S=[(-b - np.sqrt(D)) / (2*a), (-b + np.sqrt(D)) / (2*a)]
    plt.scatter(S, [0, 0], color='red', label='Racines')
    
plt.plot(x, f)
plt.grid()
plt.title(f"f(x) = {a}x² + {b}x + {c}")
plt.show()'''

''' petit programme pour essayer de prendre en main matplotlib, je continue d'apprendre.
Le programme du dessus calcule les racines réelles d'un polynôme du second degré, le second quant à lui
modélise la fonction pôlynomiale de notre choix, temps de programmation: ~20 minutes'''

coeff = []
D = int(input("entrez le degré du polynôme: "))
for i in range(D):
    coeff.append(float(input(f"entrez le coefficient de x**{D-i}: ")))
coeff.append(float(input("entrez le terme constant: ")))
f=[]
x= np.linspace(-10, 10, 100)
for i in range(D + 1):
    f.append(coeff[i]*x**(D-i))
f_x = sum(f)

plt.plot(x, f_x)
plt.grid()
plt.show()

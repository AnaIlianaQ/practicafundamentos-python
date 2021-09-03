#libreria para generar datos
import random 

#para instalar esto necesitas 
# python -m pip install -U pip
# python -m pip install -U matplotlib
import matplotlib.pyplot as plt

print(random.randint(1,20))
#Generar un numero aleatorio
print(random.randrange(10,100,2))

#declara la lista al azar
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('lista original', lista)

#mezcal los elemento de la lista al azar
random.shuffle(lista)
print('lista mixeada', lista)

#genera una grafica de campana de GAUSS
#genera los datos de la grafica
campana = [random.gauss(1,0.5)for i in range(1000)]
plt.hist(campana, bins=15)
plt.show()
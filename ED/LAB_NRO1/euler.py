num = 10 # Numero de operaciones a imprimir 
# Seria la n de acuerdo al pizarron 

print("EULER PARA ECUACIONES DIFERENCIALES")

import math
import matplotlib.pyplot as plt


fun = input("Funcion: dy/dx = : \n")
x_init = float(input("Valor inicial de x: \n"))
y_init = float(input("Valor de y cuando x vale "+str(x_init)+": \n"))
# h = float(input("Valor de h: \n"))
b = float(input("Valor de b: \n"))
h = round((b - x_init)/(num-1),2)
num = int(input("Numero de operaciones: \n"))

valores = [x_init,y_init]
x_next = x_init # x + h Este sera el siguiente valor a evaluar
resultado = [y_init] #LISTA CON LOS VALORES DE Yi de la tabla 


# funcioncopia solo es la funcion
def evaluar(funcion_copia): #EVALUAR LA FUNCION EN (Xi, Yi) # De acuerdo al pizarron seria f(Xi, Yi)
    for x in range(2): # Solo son dos valores 
        try: prueba = int(funcion_copia[abs(funcion_copia.index(str(chr(x+120)))-1)]) # Trata de convertirlo a entero
        except: prueba = str # Si no lo puede convertir a entero, es una variable string
        if type(prueba) == int: funcion_copia = funcion_copia.replace(str(chr(x+120)),("*"+str((valores[len(valores) -2+x]))),1) # Aca simplemente verifico el tipo de datos
        else: funcion_copia = funcion_copia.replace(str(chr(x+120)),(str((valores[len(valores) -2+x]))),1)
    try: return (eval(funcion_copia)) #Solo hace que el codigo se ejecute dentro de si mismo 
    except: print("Error al ingresar datos")
    

valoresx = []
valoresy = []


#Creacion de la tabla 
print(" Xn -   Yn")
for i in range(num):
    x_next += h
    y_n = ((resultado[i]) + h*(evaluar(fun))) # Formula recursiva de euler
    resultado.append(y_n)
    valores.append(x_next)
    valores.append(y_n)

    valoresx.append(x_next)
    valoresy.append(y_n)


    print(str(round(x_next,2)) +" - " +str(round(y_n,4)))

plt.plot(valoresx, valoresy, "o")
plt.show()

# SOLUCION EXACTA
valoresysolucionexacta = []
epsilon = 2.22

for valorx in valoresx:
    valorytemporal = math.pow(epsilon, valorx**2 - 1)
    valoresysolucionexacta.append(valorytemporal)


plt.plot(valoresx, valoresysolucionexacta, "o")
plt.show()




# Prueba del maestro en pizarron 
# 2xy
# 1
# 1
# 0.333

# Prueba numero 1
# Enlace video: https://www.youtube.com/watch?v=PXdjSYPYLZ4
# 0.1*math.sqrt(y)+0.4*math.pow(x,2)
# 2
# 4
# 0.05




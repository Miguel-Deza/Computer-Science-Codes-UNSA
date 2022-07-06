# USUARIO
def evaluar(funcion_copia):
    for x in range(2): 
        try: prueba = int(funcion_copia[abs(funcion_copia.index(str(chr(x+120)))-1)]) 
        except: prueba = str 
        if type(prueba) == int: funcion_copia = funcion_copia.replace(str(chr(x+120)),("*"+str((valores[len(valores) -2+x]))),1)
        else: funcion_copia = funcion_copia.replace(str(chr(x+120)),(str((valores[len(valores) -2+x]))),1)
    try: return (eval(funcion_copia))
    except: print("Error al ingresar datos")


def evaluarNext(funcion_copia,x_next, Yi, Y_0): #EVALUAR LA FUNCION EN (Xi+1, Yi+1)
        y = Y_0 + h*(Yi)
        nums = [x_next, y]
        for x in range(2):
            try: prueba = int(funcion_copia[abs(funcion_copia.index(str(chr(x+120)))-1)])
            except: prueba = str
            if type(prueba) == int: funcion_copia = funcion_copia.replace(str(chr(x+120)),("*"+str((nums[x]))),1)
            else: funcion_copia = funcion_copia.replace(str(chr(x+120)),(str(nums[x])),1)
        try: return (eval(funcion_copia))
        except: print("Error al ingresar datos")

# Euler mejorado 
print("EULER MEJORADO PARA ECUACIONES DIFERENCIALES")
import math
import matplotlib.pyplot as plt

fun = input("Funcion: dy/dx = : \n")
num = int(input("Numero de operaciones: \n"))
x_init = float(input("Valor inicial de x: \n"))
y_init = float(input("Valor de y cuando x vale "+str(x_init)+": \n"))
# h = float(input("Valor de h: \n"))
b = float(input("Valor de b: \n"))
h = round((b - x_init)/(num-1),2)

valores = [x_init,y_init]
x_next = x_init 
resultado = [y_init] 

valoresx = []
valoresy = []

print(" Xn -  Yn")
for i in range(num):
    x_next += h
    Yi = evaluar(fun)
    Y_0 = resultado[i]
    y_n = ((Y_0) + (h/2)*((Yi)+evaluarNext(fun,x_next,Yi,Y_0)))
    resultado.append(y_n)
    valores.append(x_next)
    valores.append(y_n)

    valoresx.append(x_next)
    valoresy.append(y_n)


    print(str(round(x_next,2)) +" - " +str(round(y_n,4)))   


plt.plot(valoresx, valoresy, "o")
plt.show()









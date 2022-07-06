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

print("RUNGE KUTTA PARA ECUACIONES DIFERENCIALES")
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
    k_1 = evaluar(fun)
    Y_0 = resultado[i]
    k_2 = rungeMiddle(fun,k_1)
    k_3 = rungeMiddle(fun, k_2)
    k_4 = rungeK4(fun, k_3)
    y_n = resultado[i] + (h/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)
    resultado.append(y_n)
    valores.append(x_next)
    valores.append(y_n)
    print(str(round(x_next,2)) +" - " +str(round(y_n,4)))

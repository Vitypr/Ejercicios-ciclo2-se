import math

##Definir las funciones
def sumar (x,y):
    return x + y
def restar (x,y):
    return x - y
def multiplicar (x,y):
    return x * y
def dividir (x,y):
    return x / y
def potencia (x,y):
    return pow(x,y)
def seno(x,y):
    return math.sin (x) * y
def coseno(x,y):
    return math.cos (x) * y
def tangente(x,y):
    return math.tan (x) * y
def arcoseno(x,y):
    return math.asin (x / y)
def arcocoseno(x,y):
    return math.acos (x / y)
def arcotangente(x,y):
    return math.atan (x / y)


##imprimir menu de operaciones
print ("1.calculadora estandar")
print ("2.claculadora trigonometrica")
choice=input("ingrese la letra de la opcion 1/2:")

if choice == '1':
    print ("selecciona una operacion")
    print ("1.sumar")
    print ("2.restar")
    print ("3.multiplicar")
    print ("4.dividir")
    print ("5.potencia")
    choice=input("Ingresa una opcion 1/2/3/4/5:")
    num1 = int(input("Ingrese primer variable: "))
    num2 = int(input("Ingrese segunda variable: "))
elif choice == '2':
    print ("selecciona una operacion")
    print ("a.seno")
    print ("b.coseno")
    print ("c.tangente")
    print ("d.arcseno")
    print ("e.arcocoseno")
    print ("f.arcotangente")
    choice=input("Ingresa una opcion a/b/c/d/e/f:")
    grado = int(input("Ingrese los grados: "))
    variable = int(input("Ingrese variable: "))

    

##Condiciones de calculadora estandar
if choice == '1':
    print(num1, "+", num2, "=", sumar(num1,num2))
elif choice == '2':
    print(num1, "-", num2, "=", restar(num1,num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiplicar(num1,num2))
elif choice == '4':
    print(num1, "/", num2, "=", dividir(num1,num2))
elif choice == '5':
    print(num1, "^", num2, "=", potencia(num1,num2))
else:
    print("dato invalido")

##Condiciones de calculadora trigonometrica
if choice == 'a':
    print( grado,"seno","(", variable,")", "=", seno(grado,variable))
elif choice == 'b':
    print( grado,"coseno","(", variable,")", "=", coseno(grado,variable))
elif choice == 'c':
    print( grado,"tangente","(", variable,")", "=", tangente(grado,variable))
elif choice == 'd':
    print("arcoseno","(", grado, "/", variable,")", "=", arcoseno(grado,variable))
elif choice == 'e':
    print("arcocoseno","(", grado, "/", variable,")", "=", arcocoseno(grado,variable))
elif choice == 'f':
    print("arcotangente","(", grado, "/", variable,")", "=", arcotangente(grado,variable))
else:
    print("dato invalido")
'''
Ejercicio 2: 
Defina una función de nombre mensaje, la cual debe imprimir “Esto es Programación Avanzada”, 
la cual a través de un decorator poder imprimir el texto “Hola” y “Chau”, La salida debe ser de la forma:
Hola
Esto es Programación Avanzada.
Chau

Programar un decorador que en caso de querer dividir por 0 emita un mensaje por pantalla. Integrar en un ejemplo

Programar un decorador para que imprima la fecha y hora. Integrar en un ejemplo.

Investigar: i) Cómo invocar a 2 decoradores a la vez?
            ii) Cómo invocar a un decorador que esta programado en otro archivo?

'''

# ejercicio 2 a

print("Ejercicio 2.a")
#declaracion de la funcion decoradora
def decorador_de_mensaje(function):
    
    def funcion_de_retorno():# declaracion de la funcion de retorno o funcion envolvente (wrapper)
        print("Hola")# instrucciones previas a la funcion decorada
        function() # llamado a la funcion decorada
        print("Chau") # instrucciones posteriores a la funcion decorada
        
    return funcion_de_retorno # retorno de la funcion de retorno
        
        
@decorador_de_mensaje # referencia a la funcion decoradora
def mensaje(): # declaracion de una funcion a decorar
    print("Esto es programacion avanzada")
    
    
mensaje() # llamada a la funcion decorada
print("---------------------------------------")
print("---------------------------------------")
print()
print("Ejercicio 2.b")

# EJERCICIO 2 b

#declaracion de la funcion decoradora
def decorador_dividir(function):
    
    def funcion_de_retorno(*args,**kwargs): # funcion de envoltura con toma de parametros
        print("Numerador : "+str(args[0])+ " Denominador : "+str(args[1])) # impresion de los parametros l
        
        if args[1]!=0:# condicional para ejecutar o no la funcion decorada
            
            resultado = function(*args) # asignamos a una variable el resultado que retorna la funcion decorada
            return resultado# retornamos el resultado
        else:# codigo a ejecutar en caso de que el denominador sea cero
            print("no se puede dividir por cero")
        print(" calculo finalizado")    
    return funcion_de_retorno# retorno de la funcion de retorno
    
        
@decorador_dividir # referencia a la funcion decoradora
def dividir(numerador, denominador): # funcion decorada
    return numerador/denominador

print("--------------------")
a = dividir(10,5)
print(a)
print("----------------")
b= dividir(10,0)
print(b)

print("---------------------------------------")
print("---------------------------------------")
print()
print("Ejercicio 2.c")


# declaracion de la funcion decoradora

def funcion_decoradora_fecha(function):
    import datetime #importacion de datetime para extraer la fecha
    import time # importacion de time para pausar el flujo de la funcion 
    
    def envoltura():# definicion de la funcion de retorno o envultura (wrapper)
        print("se hizo un llamado a la funcion en la fecha : "+ str(datetime.datetime.now()))# impresion de la fecha en la que se llama a la funcion decorada
        function() # llamado a la funcion decorada
        for i in range(25):
            print("%",end='')
            time.sleep(0.5)
        print()
        print("espere un momento")
        time.sleep(1)
        print("la funcion finalizo en la fecha : "+ str(datetime.datetime.now()))# impresion de la fecha en la que finaliza la funcion decorada
    return envoltura # retorno de la funcion de envoltura

@funcion_decoradora_fecha# referencia a la funcion decoradora
def hacer_algo(): # declaracion de la 
    print(" estoy haciendo algo")
    
hacer_algo()


print("---------------------------------------")
print("---------------------------------------")
print()
print("Ejercicio 2.d.1")

# declaramos la primera funcion decoradora
def funcion_decoradora_1(function):
    def wrapper():
        print("dentro de la funcion decoradora 1")
        function()
        
    return wrapper

# declaramos la segunda funcion decoradora
def funcion_decoradora_2(function):
    def wrapper():
        print("dentro de la funcion decoradora 2")
        function()
        
    return wrapper

@funcion_decoradora_1 # referenciamos al primer decorador
@funcion_decoradora_2 # referenciamos al segundo decorador
def funcion_base():   # definimos la funcio base
    print("soy la funcion base")
    
funcion_base() # llamamos a la funcion

# observacion: si bien se puede ver que se ejecutan los dos decoradores, la funcion base solo se ejecuta en uno


print("---------------------------------------")
print("---------------------------------------")
print()
print("Ejercicio 2.d.2")

from decorador_externo import decorador_externo

@decorador_externo
def funcion_base_b():
    print(" soy la funcion base")

funcion_base_b()
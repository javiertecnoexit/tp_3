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

def decorador_de_mensaje(function):
    
    def funcion_de_retorno():
        print("Hola")
        function()
        print("Chau")
        
    return funcion_de_retorno
        
        
@decorador_de_mensaje
def mensaje():
    print("Esto es programacion avanzada")
    
    
mensaje()


# EJERCICIO 2 b

def decorador_dividir(function):
    
    def funcion_de_retorno(*args,**kwargs):
        print(kwargs)
        print(kwargs.values())
        if args[1]!=0:
            
            resultado = dividir()
            return resultado
        else:
            print("no se puede dividir por cero")
            
    return funcion_de_retorno
    
        
@decorador_dividir
def dividir(numerador, denominador):
    return numerador/denominador

print("--------------------")
a = dividir(10,5)
print(a)
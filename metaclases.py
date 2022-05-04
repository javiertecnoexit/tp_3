# PONCE ALVARO
# PONCE FRANCISCO



# Ejercicio 1.a: rehacer tres clases del ejercicio de la clase anterior

'''
EJERCICIO 1.B:
                LOS METODOS SE PUEDEN DEFINIR DE DOS MANERAS EN LA CREACION DE UNA CLASE MEDIANTE UNA METACLASE,
                UNA MANERA ES DENTRO DEL DICCIONARIO ASIGNANDOLE UNA CLAVE A UNA FUNCION LAMBDA.
                OTRA MANERA ES DECLARARLO FUERA DEL METODO TYPE() Y ASIGNARLE UNA CLAVE DE REFERENCIA EN EL DICCIONARIO DEL METODO TYPE()
'''
# clase cancion
#los metodos se definen por fuera de la clase
def get_titulo(self):
    return self.titulo

def get_autor(self):
    return self.autor

def set_titulo(self, nuevo_titulo):
    self.titulo = nuevo_titulo

def set_autor(self, nuevo_autor):
    self.autor = nuevo_autor
# definimos una clase mediante el metodo type
Cancion =  type('Cancion',(),{'titulo':'estoy verde', 'autor':'Charly', 'get_titulo':get_titulo, 'get_autor':get_autor, 'set_titulo':set_titulo, 'set_autor':set_autor})
# instanciamos un objeto de la clase creada anteriormente
cancion1= Cancion()
# imprimimos los valores del objeto por defecto
print(cancion1.get_titulo(), cancion1.autor)
#seteamos el atributo titulo del objeto creado mediante el metodo set_titulo
cancion1.set_titulo("Yendo de la cama al living")
# imprimimos el objeto con un atribujo seteado
print(cancion1.get_titulo(), cancion1.autor)

# clase persona

# definicion externa de los metodos que va a usar la clase creada con type()
def get_nombre(self):
    return self.nombre
    
def get_apellido(self):
    return self.apellido
    
def get_nacionalidad(self):
    return self.nacionalidad
    
def set_nombre(self, nuevo_nombre):
    self.nombre=nuevo_nombre
        
def set_apellido(self, nuevo_apellido):
    self.apellido=nuevo_apellido
    
def set_nacionalidad(self, nueva_nacionalidad):
    self.nacionalidad=nueva_nacionalidad
    
# definimos la clase mediante el metodo metaclase type()

Persona = type('Persona',(),{'nombre':'--','apellido':'--', 'nacionalidad':'--', 'get_nombre':get_nombre, 'get_apellido': get_apellido, 'get_nacionalidad':get_nacionalidad, 'set_nombre':set_nombre, 'set_apellido':set_apellido, 'set_nacionalidad':set_nacionalidad})

# creamos un objeto con la nueva clase Persona

persona1= Persona()
persona1.set_nombre("Juan")
persona1.set_apellido("Peres")
persona1.set_nacionalidad("argentino")
print(persona1.get_nombre(), persona1.get_apellido(), persona1.get_nacionalidad())


# clase punto

def Impresion(self):
    print("el punto se encuentra en la coordenada x={0} coordenada y={1}".format( str(self.x), str(self.y)))

def Opuesto(self):
    return "el punto se encuentra en la coordenada x={0} coordenada y={1}".format( str(self.x*-1), str(self.y*-1))

def get_x(self):
    return self.x
def get_y(self):
    return self.y
def set_x(self, x):
    self.x=x
def set_y(self, y):
    self.y=y

Punto = type('Punto',(),{'x':0, 'y':0,'get_x':get_x, 'get_y':get_y,'set_x':set_x,'set_y':set_y, 'impresion':Impresion, 'opuesto':Opuesto})
a= Punto()

a.impresion()
a.set_x(2)
a.set_y(4)
print()
print(a.opuesto())
        




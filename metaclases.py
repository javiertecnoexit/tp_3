# Ejercicio 1: rehacer tres clases del ejercicio de la clase anterior

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

Cancion =  type('Cancion',(),{'titulo':'---', 'autor':'---', 'get_titulo':get_titulo, 'get_autor':get_autor, 'set_titulo':set_titulo, 'set_autor':set_autor})

cancion1= Cancion()

print(cancion1.get_titulo, cancion1.autor)

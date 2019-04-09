
class Persona:

    cabello = "negro"

    def __init__(self, edad, peso, nacionalidad, altura):
        self.edad = edad
        self.peso = peso
        self.nacionalidad = nacionalidad
        self.altura = altura

    def descripcion(self):
        print(self.edad, self.peso, self.nacionalidad, self.altura)

#Herencia
class Alumno(Persona):
    def __init__(self, nombre, matricula, escuela):
        super().__init__(19, 54, "mexicana", 1.65)
        self.nombre = nombre
        slef.matricula = matricula
        self.escuela = escuela

    def descripcion(self):
        print(self.nombre, " tiene: ", self.edad, "años, pesa:", self.peso, " estudia en ", self.escuela, " y su matricula es: ", self.matricula)

#alumno = Alumno("kenny", "E123124", "ITM")
#alumno = Alumno ("andrea", "F3478", "UADY")

#jose = Persona(19, 54, "mexicana", 1.65)
#alfredo = Persona(19, 54, "mexicana", 1.65)
#jose.edad = 40
#jose.descripcion()
#alfredo.sentarse()
#jose.pararse()

from math import pi

class Figura:
    def __init__(self, nombre_figura, color):
        self.nombre_figura = nombre_figura
        self.color = color

    def area(self):
        pass

class CirculoVerde(Figura):
    def __init__(self, nombre, radio):
        super().__init__(nombre, "Verde")
        self.nombre = nombre
        self.radio = radio

    def area(self):
        return pi*self.radio**2

class TrianguloRojo(Figura):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre, "Rojo")
        self.base = base
        self.altura = altura

    def area(self):
        return(self.base*self.altura)/2

    def suma(self, area):
        print(area+10)

    def area2(self, base, altura):
        resultado = (base*altura)/2
        print(resultado)

circulo = CirculoVerde("circulito", 4)
triangulo = TrianguloRojo("triangulo equilatero", 3, 4)
print(circulo.nombre)
print(triangulo.nombre_figura)
print(circulo.area())


#Método con return
print(triangulo.area())
#Método con print
triangulo.area2(triangulo.base, triangulo.altura)
#Método con print dentro de print
print(triangulo.area2(triangulo.base, triangulo.altura))

triangulo.suma(triangulo.area())

#triagulo.suma(triangulo.area2(triangulo.base, triangulo. altura))

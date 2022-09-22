#!/usr/bin/python3
class Alumno:
    nombre = ""
    nota = 10
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def setNota(self, nota):
        self.nota = nota

    def getNombre(seft):
        return seft.nombre

    def getNota(seft):
        return seft.nota

pedro = Alumno()
pedro.setNombre("Pedro Sanchez")
pedro.setNota(3)

print ("El alumno ", pedro.getNombre(), 
        " tiene una nota de ", pedro.getNota())

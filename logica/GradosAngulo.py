import math

pi = math.pi

class GradosAngulo():
    def __init__ (self, convertir_a_sexagesimal, angulo_sexagesimales, angulo_radianes):
        self.convertir_a_sexagesimal = convertir_a_sexagesimal
        self.angulo_sexagesimales = angulo_sexagesimales
        self.angulo_radianes = angulo_radianes

    def convertir (self):
        if (self.convertir_a_sexagesimal == 1): 
            self.angulo_sexagesimales = self.angulo_radianes * (180 / pi)
        else: 
            self.angulo_radianes = self.angulo_sexagesimales * (pi / 180)
        
    def imprimirResultado (self):
        if (self.convertir_a_sexagesimal == 1):
            print(f"El ángulo en grados sexagesimales es: {self.angulo_sexagesimales}°\n")
        else:
            print(f"El ángulo en grados radianes es: {self.angulo_radianes}rad\n")
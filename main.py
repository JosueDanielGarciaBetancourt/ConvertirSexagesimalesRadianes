from logica.GradosAngulo import GradosAngulo

if __name__ == '__main__':
    print("0. Convertir ángulo sexagesimal a radián\n1. Convertir ángulo radián a sexagesimal\n")

    convertir_a_sexagesimal = int(input("Elige una opción (0/1): "))

    if  convertir_a_sexagesimal == 1: 
        angulo_radianes = float(input("\nIngrese el valor del ángulo en radianes: "))
        angulo_sexagesimales = 0
    else: 
        angulo_sexagesimales = float(input("\nIngrese el valor del ángulo en sexagesimales: "))
        angulo_radianes = 0
       
    GradosAngulo = GradosAngulo(convertir_a_sexagesimal, angulo_sexagesimales, angulo_radianes)
    GradosAngulo.convertir()
    GradosAngulo.imprimirResultado()
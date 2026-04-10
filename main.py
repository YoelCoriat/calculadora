import Operaciones

def input_float(mensaje):
    while True:
        valor = input(mensaje)
        try:
            numero = float(valor)
            return numero
        except ValueError:
            print("Por favor ingresar un numero valido.")

def input_int(mensaje):
    while True:
        valor = input(mensaje)
        try:
            numero = int(valor)
            if numero < 1 or numero > 4:
                print("Por favor ingresar un numero entero valido.")
            else:
                return numero
        except ValueError:
            print("Por favor ingresar un numero entero valido.")


run = True
while run:
    num1 = input_float("Ingrese el primer numero: ")
    num2 = input_float("Ingrese el segundo numero: ")
    tipo_operacion = input_int("Ingrese el numero del tipo operacion que quiere realizar. "
                               "\nTipos de operaciones disponibles: "
                               "\n1. Sumar"
                               "\n2. Restar"
                               "\n3. Multiplicar"
                               "\n4. Dividir\n")

    if tipo_operacion == 1:
        operacion = Operaciones.sumar(num1, num2)
    elif tipo_operacion == 2:
        operacion = Operaciones.restar(num1, num2)
    elif tipo_operacion == 3:
        operacion = Operaciones.multiplicar(num1, num2)
    elif tipo_operacion == 4:
        operacion = Operaciones.dividir(num1, num2)
    else:
        print("ERROR: Operacion no disponible")
        continue

    print(operacion)
    run = False



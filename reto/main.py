"""
Crea una función llamada `dividir_numeros` que reciba como entrada dos valores proporcionados por el usuario y realice una división entre ellos. La función debe:

1. Solicitar al usuario que introduzca dos números (usando la función `input()`)
2. Convertir las entradas a números enteros
3. Realizar la división del primer número entre el segundo
4. Devolver el resultado de la división

La función debe manejar correctamente las siguientes excepciones:

- Si el usuario introduce algo que no se puede convertir a un entero, mostrar el mensaje "Error: Debes introducir un número válido"
- Si el usuario intenta dividir entre cero, mostrar el mensaje "Error: No es posible dividir entre cero"

Finalmente, independientemente de si la operación tuvo éxito o no, la función debe mostrar el mensaje "Operación finalizada".
"""

def dividir_numeros():
    # try
    try:

        # Solicitar al usuario que introduzca dos números
        
        print("Ingrese dos numeros")
        entrada1 = input("Ingrese el primer numero: ")
        entrada2 = input("Ingrese el segundo numero: ")

        # Convertir las entradas a números enteros

        num1 = int(entrada1)
        num2 = int(entrada2)
    
        # Realizar la división del primer número entre el segundo

        div = num1 / num2
        
        # Devolver el resultado de la división

        print(f"La division entre {num1} y {num2} dio: {div}")
    
    # except ____:
    except ValueError:
        print("Error: Debes introducir un número válido")
    
    # except ____:
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero")
    # finally:
    finally:
        print("Operación finalizada")


# Llamada a la función
dividir_numeros()
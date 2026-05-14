# Try-except básico: intercepta una división por cero y muestra mensaje personalizado en lugar de detener el programa
try:
    num1 = 10
    num2 = 0
    resultado_div = num1 / num2
    print(f"El resultado es: {resultado_div}")
except:
    print("¡Ups! No se puede dividir entre cero.")


# Excepciones específicas: diferencia entre un valor inválido y una división por cero según lo que ingrese el usuario
try:
    numero_input = int(input("Introduce un número: "))
    resultado_cien = 100 / numero_input
    print(f"100 dividido por {numero_input} es {resultado_cien}")
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
except ValueError:
    print("Debes introducir un número válido.")


# Excepción con variable de error: captura FileNotFoundError, accede a su mensaje y crea el archivo si no existe
try:
    with open("archivo_inexistente.txt", "r") as archivo_r:
        contenido_r = archivo_r.read()
except FileNotFoundError as error:
    print(f"Error: {error}")
    print("Creando un archivo nuevo...")
    with open("archivo_inexistente.txt", "w") as archivo_w:
        archivo_w.write("Este es un archivo nuevo")


# Múltiples excepciones en tupla: agrupa varios tipos de error bajo el mismo bloque except e imprime el tipo
try:
    archivo_datos = open("datos.txt", "r")
    valor_datos = int(archivo_datos.readline().strip())
    resultado_datos = 100 / valor_datos
except (FileNotFoundError, ValueError, ZeroDivisionError) as e_datos:
    print(f"Ocurrió un error: {type(e_datos).__name__}")
    print(f"Descripción: {e_datos}")


# Bucle con try-except: repite la solicitud de entrada hasta recibir un entero positivo válido
def obtener_edad():
    while True:
        try:
            edad = int(input("¿Cuál es tu edad? "))
            if edad < 0:
                print("La edad no puede ser negativa.")
                continue
            return edad
        except ValueError:
            print("Por favor, introduce un número entero.")

edad_usuario = obtener_edad()
print(f"Tu edad es: {edad_usuario}")


# Mal ejemplo — bloque try extenso con except genérico: captura cualquier error sin distinguir su origen
try:
    archivo_malo = open("datos.txt", "r")
    contenido_malo = archivo_malo.read()
    numeros_malos = [int(x) for x in contenido_malo.split()]
    resultado_malo = sum(numeros_malos) / len(numeros_malos)
    print(f"El promedio es: {resultado_malo}")
    archivo_malo.close()
except:
    print("Ocurrió un error")


# Buen ejemplo — bloques try específicos: cada operación tiene su propio except con mensaje útil
def calcular_promedio_archivo():
    try:
        archivo_bien = open("datos.txt", "r")
    except FileNotFoundError:
        print("El archivo 'datos.txt' no existe")
        return

    try:
        contenido_bien = archivo_bien.read()
        numeros_bien = [int(x) for x in contenido_bien.split()]
    except ValueError:
        print("El archivo contiene datos que no son números")
        archivo_bien.close()
        return

    try:
        resultado_bien = sum(numeros_bien) / len(numeros_bien)
        print(f"El promedio es: {resultado_bien}")
    except ZeroDivisionError:
        print("El archivo está vacío, no se puede calcular el promedio")

    archivo_bien.close()


# ZeroDivisionError: captura división entre cero
try:
    resultado_zero = 5 / 0
except ZeroDivisionError:
    print("No es posible dividir entre cero")


# OverflowError: captura cuando el resultado aritmético es demasiado grande para representarse
try:
    resultado_overflow = 10.0 ** 1000000
except OverflowError:
    print("El número es demasiado grande para ser representado")


# TypeError: captura operaciones entre tipos incompatibles
try:
    resultado_type = "42" + 10
except TypeError:
    print("No se pueden sumar tipos diferentes")


# ValueError: captura conversiones con valor inapropiado aunque el tipo sea correcto
try:
    numero_val = int("abc")
except ValueError:
    print("La cadena no representa un número válido")


# IndexError: captura acceso a índice fuera del rango de una lista
try:
    lista_idx = [1, 2, 3]
    elemento_idx = lista_idx[10]
except IndexError:
    print("El índice está fuera del rango de la lista")


# KeyError: captura acceso a clave inexistente en un diccionario
try:
    diccionario_key = {"nombre": "Ana", "edad": 25}
    valor_key = diccionario_key["telefono"]
except KeyError:
    print("La clave 'telefono' no existe en el diccionario")


# FileNotFoundError: captura intento de abrir un archivo que no existe
try:
    with open("archivo_inexistente2.txt", "r") as archivo_fnf:
        contenido_fnf = archivo_fnf.read()
except FileNotFoundError:
    print("El archivo no existe")


# PermissionError: captura intento de escritura en archivo sin permisos suficientes
try:
    with open("/etc/passwd", "w") as archivo_perm:
        archivo_perm.write("datos")
except PermissionError:
    print("No tienes permisos para modificar este archivo")


# AttributeError: captura acceso a atributo o método que no existe en el objeto
try:
    texto_attr = "Hola"
    longitud_attr = texto_attr.size
except AttributeError:
    print("El objeto string no tiene el atributo 'size'")


# NameError: captura uso de variable no definida
try:
    print(variable_no_definida)
except NameError:
    print("La variable no está definida")


# ImportError: captura fallo al importar un módulo
try:
    import biblioteca_inexistente
except ImportError:
    print("No se pudo importar el módulo")


# ModuleNotFoundError: subclase de ImportError, captura específicamente módulos que no existen
try:
    import modulo_que_no_existe
except ModuleNotFoundError:
    print("El módulo no existe")


# Exception genérico: captura cualquier excepción estándar e imprime su tipo y descripción
try:
    resultado_gen = int("abc") / 0
except Exception as e_gen:
    print(f"Se produjo un error: {type(e_gen).__name__}")
    print(f"Descripción: {e_gen}")


# Identificar excepción desconocida: patrón para descubrir qué tipo de excepción lanza una expresión
try:
    resultado_eval = eval(input("Introduce una expresión: "))
except Exception as e_eval:
    print(f"Error de tipo: {type(e_eval).__name__}")
    print(f"Descripción: {e_eval}")


# Excepciones de librería externa: maneja errores específicos de requests al hacer llamadas HTTP
import requests

try:
    respuesta_http = requests.get("https://api.ejemplo.com/datos", timeout=1)
    respuesta_http.raise_for_status()
except requests.exceptions.ConnectionError:
    print("No se pudo conectar al servidor")
except requests.exceptions.Timeout:
    print("La solicitud excedió el tiempo de espera")
except requests.exceptions.HTTPError as e_http:
    print(f"Error HTTP: {e_http}")


# Cláusula else: ejecuta código adicional solo si el bloque try no lanzó ninguna excepción
try:
    numero_else = int(input("Introduce un número: "))
    resultado_else = 100 / numero_else
except ValueError:
    print("Debes introducir un número válido.")
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
else:
    print(f"El resultado es: {resultado_else}")


# Else con archivo: cierra el archivo solo si se abrió y leyó correctamente
try:
    archivo_else = open("datos.txt", "r")
    contenido_else = archivo_else.read()
except FileNotFoundError:
    print("El archivo no existe.")
    contenido_else = ""
else:
    print("Archivo leído correctamente.")
    archivo_else.close()


# Finally con archivo: garantiza que el archivo se cierre siempre, ocurra o no una excepción
try:
    archivo_fin = open("registro.txt", "w")
    archivo_fin.write("Operación iniciada\n")
    resultado_fin = 10 / int(input("Introduce un número: "))
    archivo_fin.write(f"Resultado: {resultado_fin}\n")
except ZeroDivisionError:
    archivo_fin.write("Error: División por cero\n")
except ValueError:
    archivo_fin.write("Error: Valor no válido\n")
finally:
    archivo_fin.write("Operación finalizada\n")
    archivo_fin.close()
    print("Proceso completado")


# Finally con conexión a BD: cierra la conexión siempre, independientemente de si la consulta falló
def conectar_base_datos():
    pass  # placeholder

def procesar_datos_bd(d):
    pass

conexion_bd = None
try:
    conexion_bd = conectar_base_datos()
    datos_bd = conexion_bd.ejecutar_consulta("SELECT * FROM usuarios")
    procesar_datos_bd(datos_bd)
except Exception as e_bd:
    print("Error en base de datos")
finally:
    if conexion_bd:
        conexion_bd.cerrar()


# Finally con modo de sistema: restaura el estado original del sistema aunque la actualización falle
def obtener_modo():
    pass

def cambiar_modo(m):
    pass

def realizar_actualizacion():
    pass

modo_original = obtener_modo()
try:
    cambiar_modo("mantenimiento")
    realizar_actualizacion()
except Exception:
    print("La actualización falló")
finally:
    cambiar_modo(modo_original)


# Else y finally combinados: else solo si no hubo error, finally siempre cierra el archivo
try:
    archivo_combo = open("datos.txt", "r")
    contenido_combo = archivo_combo.read()
except FileNotFoundError:
    print("El archivo no existe, se creará uno nuevo.")
    archivo_combo = open("datos.txt", "w")
    archivo_combo.write("Archivo creado automáticamente")
else:
    print(f"Contenido leído: {contenido_combo}")
finally:
    print("Operación de archivo completada.")
    archivo_combo.close()


# Orden de ejecución: muestra en qué secuencia corren try, except, else y finally
def demostrar_orden():
    try:
        print("1. Ejecutando bloque try")
    except ZeroDivisionError:
        print("2. Ejecutando bloque except")
    else:
        print("3. Ejecutando bloque else")
    finally:
        print("4. Ejecutando bloque finally")
    print("5. Continuando después del bloque try")

demostrar_orden()


# Return con finally: finally se ejecuta antes de devolver cualquier valor, sin importar desde qué bloque se retorne
def dividir_retorno(a, b):
    try:
        resultado_ret = a / b
        return resultado_ret
    except ZeroDivisionError:
        print("Error: División por cero")
        return None
    finally:
        print("División finalizada")

print(dividir_retorno(10, 2))
print(dividir_retorno(10, 0))


# Raise básico: lanza una excepción manualmente antes de que Python la detecte por su cuenta
def dividir_raise(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b

try:
    resultado_raise = dividir_raise(10, 0)
except ZeroDivisionError as e_raise:
    print(f"Error: {e_raise}")


# Raise con validación de dominio: lanza ValueError si el argumento tiene un valor fuera del rango permitido
def calcular_raiz_cuadrada(numero_raiz):
    if numero_raiz < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return numero_raiz ** 0.5


# Raise para estados inesperados: lanza RuntimeError cuando el código recibe un caso no contemplado
def procesar_respuesta(respuesta):
    if respuesta.codigo == 200:
        return respuesta.datos
    elif respuesta.codigo == 404:
        return None
    else:
        raise RuntimeError(f"Código de respuesta no manejado: {respuesta.codigo}")


# Raise con precondiciones: valida múltiples condiciones al inicio y lanza ValueError si alguna falla
def retirar_dinero(cuenta, cantidad_retiro):
    if not cuenta.esta_activa:
        raise ValueError("La cuenta no está activa")
    if cantidad_retiro <= 0:
        raise ValueError("La cantidad debe ser positiva")
    if cantidad_retiro > cuenta.saldo:
        raise ValueError("Saldo insuficiente")
    cuenta.saldo -= cantidad_retiro
    return cuenta.saldo


# Raise con TypeError y ValueError: valida tanto el tipo como el rango del argumento
def establecer_edad(edad_set):
    if not isinstance(edad_set, int):
        raise TypeError("La edad debe ser un número entero")
    if edad_set < 0 or edad_set > 150:
        raise ValueError("La edad debe estar entre 0 y 150 años")
    return edad_set


# Raise TypeError en dos argumentos: valida que ambos parámetros sean del tipo esperado antes de operar
def concatenar(texto_concat, repeticiones_concat):
    if not isinstance(texto_concat, str):
        raise TypeError("El primer argumento debe ser una cadena de texto")
    if not isinstance(repeticiones_concat, int):
        raise TypeError("El segundo argumento debe ser un número entero")
    return texto_concat * repeticiones_concat


# Relanzar excepción: captura el error, lo registra, y lo vuelve a lanzar para que suba al nivel superior
def procesar_archivo_relanzar(ruta_relanzar):
    try:
        with open(ruta_relanzar, 'r') as archivo_relanzar:
            return archivo_relanzar.read()
    except FileNotFoundError as e_relanzar:
        print(f"Registrando error: {e_relanzar}")
        raise


# Encadenar excepciones con from: convierte una excepción técnica en una de dominio, preservando la causa original
def obtener_configuracion(archivo_cfg):
    try:
        with open(archivo_cfg, 'r') as f_cfg:
            return f_cfg.read()
    except FileNotFoundError as e_cfg:
        raise RuntimeError(f"Archivo de configuración no encontrado: {archivo_cfg}") from e_cfg


# Excepción personalizada: clase propia con datos específicos del error (saldo, cantidad, déficit)
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_ins, cantidad_ins):
        self.saldo = saldo_ins
        self.cantidad = cantidad_ins
        self.deficit = cantidad_ins - saldo_ins
        mensaje = f"No hay suficiente saldo. Saldo: {saldo_ins}, Cantidad solicitada: {cantidad_ins}"
        super().__init__(mensaje)

def retirar_custom(cuenta_custom, cantidad_custom):
    if cantidad_custom > cuenta_custom.saldo:
        raise SaldoInsuficienteError(cuenta_custom.saldo, cantidad_custom)
    cuenta_custom.saldo -= cantidad_custom
    return cuenta_custom.saldo


# Validación temprana con raise: verifica parámetros al inicio de la función para fallar lo antes posible
def procesar_datos_validados(datos_val):
    if datos_val is None:
        raise ValueError("Los datos no pueden ser None")
    if not isinstance(datos_val, list):
        raise TypeError("Los datos deben ser una lista")
    if len(datos_val) == 0:
        raise ValueError("La lista de datos no puede estar vacía")
    resultado_val = []
    for item_val in datos_val:
        pass  # procesamiento


# Obtener edad con raise interno: lanza ValueError explícito para entradas vacías o fuera de rango, además del ValueError de int()
def obtener_edad_completa():
    while True:
        try:
            entrada_edad = input("Introduce tu edad: ")
            if not entrada_edad.strip():
                raise ValueError("La entrada no puede estar vacía")
            edad_completa = int(entrada_edad)
            if edad_completa < 0:
                raise ValueError("La edad no puede ser negativa")
            if edad_completa > 120:
                raise ValueError("La edad parece demasiado alta")
            return edad_completa
        except ValueError as e_edad:
            if str(e_edad).startswith("invalid literal for int"):
                print("Por favor, introduce un número válido")
            else:
                print(f"Error: {e_edad}")

try:
    edad_final = obtener_edad_completa()
    print(f"Tu edad es: {edad_final}")
except KeyboardInterrupt:
    print("\nOperación cancelada por el usuario")
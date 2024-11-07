# Ejercicios de Decoradores

# Ejercicio 1: Decorador de Tiempo de Ejecución
# Crea un decorador llamado tiempo_ejecucion que mida y muestre el tiempo de ejecución de una función.

import time

def tiempo_ejecucion(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        resultado = func(*args, **kwargs)
        end = time.time()
        print("Tiempo de ejecución:", (end - start) * 1000)
        return resultado
    return wrapper

@tiempo_ejecucion
def calcula_nada(n):
    print("calcula_nada:", n)
    for x in range(1, n):
        for y in range(1, n):
            x**y

print("--------------------------------")

calcula_nada(100)
calcula_nada(500)

# Ejercicio 2: Decorador de Registro de Parámetros
# Crea un decorador llamado registrar que imprima los argumentos con los que fue llamada una función y el resultado que devuelve.

def registrar(func):
    def wrapper(*args, **kwargs):
        print("Args:", args)
        print("Kwargs:", kwargs)
        ret = func(*args, **kwargs)
        print("Ret:", ret)
        return ret
    return wrapper

@registrar
def multiplica(a, b, c):
    return a * b * c

@registrar
def voltea(s):
    return(s[::-1])

@registrar
def saluda(nombre, origen):
    print("hola {0} de {1}")

print("--------------------------------")
multiplica(1,2,3)
voltea("hola")
saluda(nombre="Manuel", origen="Mexico")

# Ejercicio 3: Decorador de Autenticación
# Crea un decorador llamado autenticacion que reciba un parámetro usuario_autenticado (un booleano) y permita ejecutar la función solo si el usuario está autenticado.
# Si no está autenticado, muestra un mensaje de error.

def autenticacion(usuario_autentificado):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if usuario_autentificado:
                return func(*args, **kwargs)
            else:
                print("Acceso denegado")
        return wrapper
    return decorator

@autenticacion(usuario_autentificado=False)
def uno():
    print("Exito uno!")

@autenticacion(usuario_autentificado=True)
def dos():
    print("Exito dos!")

print("--------------------------------")
uno()
dos()

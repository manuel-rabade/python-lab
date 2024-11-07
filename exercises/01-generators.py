from typing import *

# Ejercicios de Generadores

# Ejercicio 1: Generador de Números Pares
# Crea un generador llamado pares que reciba un número n y devuelva los primeros n números pares, uno a uno.

def pares(n):
    for p in range(2, n * 2 + 1, 2):
        yield p

print("--------------------------------")
for p in pares(6):
    print (p)

# Ejercicio 2: Generador Infinito de Fibonacci
# Crea un generador fibonacci que genere números de la secuencia de Fibonacci indefinidamente. Detén la ejecución manualmente cuando hayas probado los primeros 10 valores.

def fibonacci():
    n_2 = 0
    n_1 = 1
    while True:
        n = n_1 + n_2
        yield n
        n_2 = n_1
        n_1 = n

print("--------------------------------")
i = 0
for x in fibonacci():
    print(i, x)
    i += 1
    if i == 10:
        break

# Ejercicio 3: Generador de Palabras Largas
# Crea un generador palabras_largas que reciba una lista de palabras y un número entero n, y devuelva solo las palabras que tengan más de n caracteres.

def palabras_largas(palabras: List[str], n: int) -> Generator[str,None,None]:
    for w in palabras:
        if len(w) > n:
            yield w

print("--------------------------------")
for p in palabras_largas([ 'hola', 'amigo', 'como', 'estas', 'uno', 'dos', 'tres', 'mundo'], 3):
    print(p)

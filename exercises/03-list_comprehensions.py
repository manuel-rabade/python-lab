# Ejercicios de Listas por Comprensión

# Ejercicio 1: Cuadrados de Números Pares
# Usa una lista por comprensión para crear una lista que contenga el cuadrado de los números pares del 1 al 10.

cuadrados = [ x**2 for x in range(1,11) if x % 2 == 0 ]
print("cuadrados:", cuadrados)

# Ejercicio 2: Filtrar Palabras con Letras Específicas
# Dada una lista de palabras, usa una lista por comprensión para crear una nueva lista que contenga solo las palabras que empiezan con la letra "P".

lista_palabras = [ "hola", "amigo", "perfecto", "balcon", "pito" ]
nueva_lista = [ x for x in lista_palabras if x.startswith("p") ]
print(nueva_lista)

# Ejercicio 3: Crear Diccionario de Longitudes de Palabras
# Usa una lista por comprensión para crear un diccionario que tenga como claves las palabras de una lista y como valores la longitud de cada palabra.

dict_lens = { x: len(x) for x in lista_palabras }
print(dict_lens)

# Ejercicio 4: Números Divisibles por 3 y 5
# Usa una lista por comprensión para crear una lista que contenga los números del 1 al 50 que sean divisibles tanto por 3 como por 5.

multiplos_3_5 = [ x for x in range(1,51) if x % 3 == 0 and x % 5 == 0]
print(multiplos_3_5)

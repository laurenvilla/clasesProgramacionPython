# altura = 10#int(input())

# for c in range(1,altura+1):
#   print( ' '*(altura-c)  +  "*"*c)

# for i in range(10):
#   for j in range(10-i):
#       print(' ',end='')
#   for j in range(i):
#       print('*',end='')
#   print()

# for numeroDeAsteriscos in range(0,altura+1):
#     asteriscos = '*'
#     for i in range(numeroDeAsteriscos):
#         asteriscos += '*'
#     print(asteriscos)

# asteriscos = ''
# for contador in range(0,altura+1):
#     asteriscos += '*'
#     print(asteriscos)

# for numAsteriscos in range(1,altura+1):
#     for contador in range(numAsteriscos):
#         print('*',end='')
#     print()



# # print('         ' +'*')
# # # *
# # print('        '  +'**')
# # # **
# # print('       '  +'***')

# # print('***')
# # ***
# # ****
# # *****
# # ******
# # *******
# # ********
# # *********
# # **********

# split()
# Input: Una oracion
# Output: Una lista con las palabras de la oracion separadas por espacios.
# si termina con espacio no debe regresar la palabra vacia
oracion='welcome to the jungle'
listaPalabras = list()
palabra=''
for letra in oracion:
    if letra == ' ':
    # necesitamos borrar el buffer de palabra
    # a partir del espacio es cuando queremos que reconozca que es un nuevo
    # valor
    # guardamos la palabra construida
      listaPalabras.append(palabra)
      palabra=''
    else:
    # construyendo la palabra que vamos a guardar
      palabra+= letra
# no queremos agregar la palabra si esta vacia
if palabra != '':
  listaPalabras.append(palabra)

print(listaPalabras)

oracion = 'hola Mundo'

# Recorremos letra por letra


#checar si es mayuscula -> en ascii esta entre 'A' y 'Z'
  #Terminar anticipado 
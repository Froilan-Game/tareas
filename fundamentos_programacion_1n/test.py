#se importa math para usar floor y re (regex) para usar las regex y comparar el resultado mas tarde
import math
import re
try:
  num = int(input("ingresa un numero entero positivo de entre 0 y 100: "))
except:
  num = -1

"""
no se puede sacar binario a un numero negativo, por esto 
se validad a que el numero ingresado no sea
negativo
"""
while num < 0 or num > 100:
  print("El numero ingresado es incorrecto, debe ser un numero entero entre 0 y 100")

  try:
    num = int(input("ingresa un numero entero positivo de entre 0 y 100: "))
  except:
    num = -1

cpy = num
""" se inicializa la variable binario para que en caso de que sea 1  
su binario sea 1, caso contraio 0. Esto se hace con el fin de que si 
se ingresa un 1 no entre al while y 1 en binario es 1, en caso de 
que se ingrese un numero diferente de 1, por ejemplo 0, su binario es 0"""
binario = "1" if num == 1 else "0"

while num > 1:
  
  if num == cpy:
    binario = ""

  #print(num, "| 2\n r:", num%2," |", math.floor(num/2))

  """ la condicional de num == 2 es en caso de que 2|2 no de un 1 que es del
   residuo, si no que de 11 contando el del cociente
  lo mismo para el 3, 3|2 que no de un unico 1 del residuo si no que cuente
  el cociente y sea 11 """
  if num == 2:
    binario = binario + "01"
  elif num == 3:
    binario = binario + "11"
  elif num % 2 == 0:
    binario = binario + "0"
  else:
    binario = binario + "1"

  #num ahora sera la division entre 2 redondeada al mas bajo, es decir:
  # 1.75 != 2, 1.75 = 1

  num = math.floor(num/2)

print("la transformacion de decimal a binario del numero: ",cpy," es: ", binario[::-1])

print("\n----- COMPROBACION -----\n")

""" se compara el resultado de lo que dio la variable "binario" con lo que retorna
la funcion bin(), re.sub() es una funcion que se usa para reemplazar el 0b 
que retorna al inicio de la cadena de texto bin(), bin(20) retun 0b10100
se reemplaza el "0b" por un espacio """
print(" ", binario[::-1],"<- programa", "\n", re.sub("0b"," ",bin(int(cpy))),"<- funcion")
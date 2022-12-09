from Figure import Figure
from Diamond import Diamond
from Parallelogram import Parallelogram
from Rectangle import Rectangle
from Square import Square
from Triangle import Triangle

while True:
    try:
        size = int(input(
            "ingresa el diametro de las figuras, que no sea mayor a 10 ni menor a 1: "))
    except:
        print("solo puedes ingresar numeros enteros")

    if 0 < size <= 10:
        break
    else:
        print("El diametro no puede ser un numero negativo o mayor a 10")

triangle = Figure(Triangle, size)
square = Figure(Square, size)
rectangle = Figure(Rectangle, size)
diamond = Figure(Diamond, size)
parallelogram = Figure(Parallelogram, size)

figures = (triangle, square, diamond, parallelogram, rectangle)

for i in figures:
  print(i.__type__())
  print(i.__figure__())

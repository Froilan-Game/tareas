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

contour = "#"
partsDiamond = []
diamond = ""

for x in range(size):
    partsDiamond.append(contour.center(size*2+1, " "))
    contour += " #"

for i in partsDiamond:
    diamond += i+"\n"

for i in range(len(partsDiamond)-1, 0, -1):
    diamond += str(partsDiamond[i-1]) + "\n"

print(diamond)

contour = ""
partsParallelogram = []
figureParallelogram = ""


for x in range(size):
  contour += " #"

for x in range(size):
  partsParallelogram.append("".join(list(reversed(contour))))
  contour += " "

for i in range(len(partsParallelogram), 0, -1):
  figureParallelogram += str(partsParallelogram[i-1]) + "\n"

print(figureParallelogram)

contour = ""
partsRectangle = []
figureRectamgle = ""


for x in range(size):
  contour += " # #"

for x in range(size):
  partsRectangle.append(contour)

for i in partsRectangle:
  figureRectamgle += i + "\n"

print(figureRectamgle)

contour = ""
partsSquare = []
figureSquare = ""


for x in range(size):
  contour += " #"

for x in range(size):
  partsSquare.append(contour)

for i in partsSquare:
  figureSquare += i + "\n"

print(figureSquare)

contour = "#"
partsTriangle = []
figureTriangle = ""

for x in range(size):
  partsTriangle.append(contour.center(size*2+1, " "))
  contour += " #"

for i in partsTriangle:
  figureTriangle += i+"\n"

print(figureTriangle)

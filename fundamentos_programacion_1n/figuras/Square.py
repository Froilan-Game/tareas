class Square:
  """clase para la figura "cuadrado"
  `size = size : number`
  """

  _type = "square"

  def __init__(self, size):

    self._size = size
    self._contour = ""
    self.parts = []
    self._figure = ""

  def get_figure(self):
    """
    retorna la figura "cuadrado"
    """

    for x in range(self._size):
      self._contour += " #"

    for x in range(self._size):
      self.parts.append(self._contour)

    for i in self.parts:
      self._figure += i + "\n"

    return self._figure


if __name__ == "__main__":
    sqr = Square(10)
    print(sqr.get_figure())

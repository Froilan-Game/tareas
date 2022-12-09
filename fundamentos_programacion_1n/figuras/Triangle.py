class Triangle:
  """clase para la figura "triangulo"
  `size = size : number`
  """

  _type = "triangle"

  def __init__(self, size):

    self._size = size
    self._contour = "#"
    self.parts = []
    self._figure = ""

  def get_figure(self):
    """
    retorna la figura "triangulo"
    """

    for x in range(self._size):
      self.parts.append(self._contour.center(self._size*2+1, " "))
      self._contour += " #"

    for i in self.parts:
      self._figure += i+"\n"

    return self._figure


if __name__ == '__main__':
    tri = Triangle(10)
    print(tri.get_figure())

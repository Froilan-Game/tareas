class Rectangle:
  """clase para la figura "rectangulo"
  `size = size : number`
  """

  _type = "rectangle"

  def __init__(self, size):

    self._size = size
    self._contour = ""
    self.parts = []
    self._figure = ""

  def get_figure(self):
    """
    retorna la figura "rectangulo"
    """

    for x in range(self._size):
      self._contour += " # #"

    for x in range(self._size):
      self.parts.append(self._contour)

    for i in self.parts:
      self._figure += i + "\n"

    return self._figure


if __name__ == "__main__":
    rec = Rectangle(10)
    print(rec.get_figure())

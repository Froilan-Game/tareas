class Diamond:
  """clase para la figura "rombo"
  `size = size : number`
  """

  _type = "diamond"

  def __init__(self, size):

    self._size = size
    self._contour = "#"
    self.parts = []
    self._figure = ""

  def get_figure(self):
    """
    retorna la figura "rombo"
    """

    for x in range(self._size):
      self.parts.append(self._contour.center(self._size*2+1, " "))
      self._contour += " #"

    for i in self.parts:
      self._figure += i+"\n"

    for i in range(len(self.parts)-1, 0, -1):
      self._figure += str(self.parts[i-1]) + "\n"

    return self._figure


if __name__ == '__main__':
    newDiamond = Diamond(10)
    print(newDiamond.get_figure())

class Parallelogram:
  """clase para la figura "paralelogramo"
  `size = size : number`
  """

  _type = "parallelogram"

  def __init__(self, size):

    self._size = size
    self._contour = ""
    self.parts = []
    self._figure = ""

  def get_figure(self):
    """
    retorna la figura "paralelogramo"
    """

    for x in range(self._size):
      self._contour += " #"

    for x in range(self._size):
      self.parts.append("".join(list(reversed(self._contour))))
      self._contour += " "

    for i in range(len(self.parts), 0, -1):
      self._figure += str(self.parts[i-1]) + "\n"

    return self._figure


if __name__ == "__main__":
    para = Parallelogram(10)
    print(para.get_figure())

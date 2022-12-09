class Figure:
  """Figure es una clase de duck typing creada para retornar algunos metodos y funciones de una clase con determinados metodos y funciones
  `class_name = class : class`
  `size = size : number`
  """
  
  def __init__(self, class_name, size):
    self.cls = class_name(size)

  def __figure__(self):
    """
    `retorna una figura creada por la clase pasada como parametro al inicializar `
    """
    return self.cls.get_figure()

  def __type__(self):
    """retorna el tipo de figura de la clase pasada como parametro al inicializar"""
    return "\n" + self.cls._type + "\n"
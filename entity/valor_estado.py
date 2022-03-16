from operator import attrgetter

class ValorEstado:
  def __init__(self, estado, valor=0) -> None:
      self.valor = valor
      self.estado = estado
  
  @staticmethod
  def max_valor_estado(valores_estados):
    return max(valores_estados, key=attrgetter('valor'))
  
  @staticmethod
  def min_valor_estado(valores_estados):
    return min(valores_estados, key=attrgetter('valor'))
from entity.valor_estado import ValorEstado
from verificador import verifica_resultado


def gera_possiveis_proximos_estados(estado_de_partida, simbolo_a_jogar):
  lista_valores_estados = []
  for i in range(3):
    for j in range(3):
      if(estado_de_partida[i][j]=='_'):
        estado_possivel = [list(estado_de_partida[0]),list(estado_de_partida[1]), list(estado_de_partida[2])]
        estado_possivel[i][j] = simbolo_a_jogar
        lista_valores_estados.append(ValorEstado(estado_possivel, 0))
  return lista_valores_estados


def vez_max(estado):
  resultado = verifica_resultado(estado)
  if(resultado):
    return ValorEstado(estado, resultado)

  lista_valores_estados = gera_possiveis_proximos_estados(estado, 'X')
  
  for i in range(len(lista_valores_estados)):
    valor_estado_resultado_min = vez_min(lista_valores_estados[i].estado)
    lista_valores_estados[i].valor = valor_estado_resultado_min.valor
  
  return ValorEstado.max_valor_estado(lista_valores_estados)


def vez_min(estado):
  resultado = verifica_resultado(estado)
  if(resultado):
    return ValorEstado(estado, resultado)
  
  lista_valores_estados = gera_possiveis_proximos_estados(estado, 'O')

  for i in range(len(lista_valores_estados)):
    valor_estado_resultado_max = vez_max(lista_valores_estados[i].estado)
    lista_valores_estados[i].valor = valor_estado_resultado_max.valor
  
  return ValorEstado.min_valor_estado(lista_valores_estados)
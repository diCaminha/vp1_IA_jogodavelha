from verificador import verifica_resultado

def vez_max(estado):
  estado_final = verifica_resultado(estado)
  if(estado_final):
    return [estado_final, estado]
  acoes = []
  for i in range(3):
    for j in range(3):
      if(estado[i][j]=='_'):
        copia = [list(estado[0]),list(estado[1]), list(estado[2])]
        copia[i][j] = 'X'
        acoes.append([0, copia])
  for i in range(len(acoes)):
    acoes[i][0] = vez_min(acoes[i][1])[0]
  return max(acoes)


def vez_min(estado):
  estado_final = verifica_resultado(estado)
  if(estado_final):
    return [estado_final, estado]
  acoes = []
  for i in range(3):
    for j in range(3):
      if(estado[i][j]=='_'):
        copia = [list(estado[0]),list(estado[1]), list(estado[2])]
        copia[i][j] = 'O'
        acoes.append([0, copia])
  for i in range(len(acoes)):
    acoes[i][0] = vez_max(acoes[i][1])[0]
  return min(acoes)
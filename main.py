from min_max import vez_max, vez_min
from verificador import verifica_resultado


def main():
    vez_maquina = True
    continuar = True
    while(continuar):
        jogada_max = True
        estado = cria_estado_inicial()
        while(not verifica_resultado(estado)):
            if vez_maquina:
               # if jogada_max:
               #     estado = vez_max(estado).estado
               # else:
               #     estado = vez_min(estado).estado
               estado = vez_max(estado).estado
            else:
                print('Jogador [O]: ')
                valor = 'O'
                linha = int(input('informe a linha (1 a 3): '))
                coluna = int(input(f'informe que coluna da linha {linha}: '))
                estado[linha-1][coluna-1] = valor

            if vez_maquina:
              print("Maquina jogou: ")
            else:
              print("Voce jogou: ")
            printa_estado(estado)

            vez_maquina = not vez_maquina
            jogada_max = not jogada_max

        resultado_final = verifica_resultado(estado)
        if resultado_final == 1:
            print("vitoria O")
        elif resultado_final == 2:
            print("Empate")
        else:
            print("vitoria X")
        
        jogar = input("jogar novamente? (S) ou (N):")
        if jogar == 'S':
          continuar = True
          vez_maquina = True
        else:
          continuar = False


def __cria_estado_inicial():
  curr_estado = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']]
  
  return curr_estado


def __printa_estado(estado):
  print('  1 2 3')
  for i in range(3):
      print('%d' % (i+1), *estado[i],'', sep = '|')


main()

from min_max import vez_max, vez_min
from verificador import verifica_resultado

curr_estado = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]

def cria_estado_inicial():
    return curr_estado

def printa_estado(estado):
  print('  1 2 3')
  for i in range(3):
      print('%d' % (i+1), *estado[i],'', sep = '|')

def main():
    vez_maquina = True
    jogar = 'S'
    while(jogar == 'S'):
        primeira_jogada = True
        estado = cria_estado_inicial()
        printa_estado(estado)
        while(not verifica_resultado(estado)):
            if vez_maquina:
                if primeira_jogada:
                    estado = vez_max(estado).estado
                else:
                    estado = vez_min(estado).estado
            else:
                print('Jogador [O]: ')
                valor = 'O'
                linha = int(input('linha: '))
                coluna = int(input('coluna: '))
                estado[linha-1][coluna-1] = valor

            vez_maquina = not vez_maquina
            primeira_jogada = not primeira_jogada
            printa_estado(estado)

        resultado_final = verifica_resultado(estado)
        if resultado_final == 1:
            print("vitoria O")
        elif resultado_final == 2:
            print("Empate")
        else:
            print("vitoria X")
        
        jogar = input("jogar novamente? (S) ou (N):")

main()
"""
0 - nao terminou
1 - vitoria de O
2 - empate 
3 - vitoria de X
"""
def verifica_resultado(estado):
    if verifica_vitoria(estado, 'O'):
        return 1
    elif verifica_vitoria(estado, 'X'):
        return 3

    for i in range(3):
        if '_' in estado[i]:
            return 0
    
    return 2


def verifica_vitoria(estado, simbolo):
    for i in range(0, 3):
        if estado[i][0] == simbolo and estado[i][1] == simbolo and estado[i][2] == simbolo:
            return True

    for i in range(0, 3):
        if estado[0][i] == simbolo and estado[1][i] == simbolo and estado[2][i] == simbolo:
            return True

    if estado[0][0] == simbolo and estado[1][1] == simbolo and estado[2][2] == simbolo:
        return True
    
    if estado[0][2] == simbolo and estado[1][1] == simbolo and estado[2][0] == simbolo:
        return True
    
    return False
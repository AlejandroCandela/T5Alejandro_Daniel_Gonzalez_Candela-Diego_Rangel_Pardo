def gato():
    return [['','',''],['','',''],['','','']] 
            
def minimax_a_b():
    tablero = gato()
    return max_jugada(tablero,-2**32,2**32)

def ganador(estado):
    for i in range(3):
        if  (estado[0][i] == 'o' and estado[1][i] == 'o' and estado[2][i] == 'o') or (estado[i][0] == 'o'  and estado[i][1] == 'o' and estado[i][2] == 'o'):
            return -1
        elif (estado[0][i] == 'x' and estado[1][i] == 'x' and estado[2][i] == 'x') or (estado[i][0] == 'x'  and estado[i][1] == 'x' and estado[i][2] == 'x'):
            return 1
        
    if (estado[0][0] == 'o' and estado[1][1] == 'o' and estado[2][2] == 'o') or (estado[2][0] == 'o' and estado[1][1] == 'o' and estado[0][2] == 'o'):
        return -1
    elif (estado[0][0] == 'x' and estado[1][1] == 'x' and estado[2][2] == 'x') or (estado[2][0] == 'x' and estado[1][1] == 'x' and estado[0][2] == 'x'):
        return 1
    for i in range(3):
        for j in range(3):
            if estado[i][j] == '':
                return 2
    return 0

def posibles_jugadas(estado, jugador):
    posibles_jugadas = []
    for i in range(3):
        for j in range(3):
            if estado[i][j] == '':
                l = [estado[0][:],estado[1][:],estado[2][:]]
                if jugador == True:
                    l[i][j] = 'x'
                    posibles_jugadas.append(l)
                else:
                    l[i][j] = 'o'
                    posibles_jugadas.append(l)
    return posibles_jugadas

def min_jugada(estado,alfa,beta):
    gano = ganador(estado)
    if gano == 1 or gano == -1 or gano == 0:
        return gano, estado
    valor = 2**32
    for i in posibles_casillas(estado,False):
        valor_p, estado_p = max_jugada(i,alfa,beta)
        #valor = min(valor, max_jugada)
        if valor >= valor_p:
            valor = valor_p
            estado = estado_p
        if valor <= alfa:
            return valor, estado
        beta = min(beta,valor)
    return valor, estado

def max_jugada(estado,alfa,beta):
    if ganador(estado) == 1 or ganador(estado) == -1 or ganador(estado) == 0:
        return ganador(estado), estado
    valor = -2**32
    for i in posibles_casillas(estado,True):
        valor_p, estado_p = min_jugada(i,alfa,beta)
        #valor = max(valor, min_jugada)
        if valor <= valor_p:
            valor = valor_p
            estado = estado_p
        if valor >= beta:
            return valor, estado
        alfa = max(alfa,valor)
    return valor, estado

valor, estado = minimax_a_b()
print(valor)
for i in estado:
    print(i)
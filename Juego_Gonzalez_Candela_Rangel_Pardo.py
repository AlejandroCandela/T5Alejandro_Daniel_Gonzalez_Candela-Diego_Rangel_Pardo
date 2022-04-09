import time

def gato():
    return [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] 
            
def minimax_a_b(tablero): 
    return max_jugada_a_b(tablero,-2**32,2**32) ## Iniciamos el juego con max tendremos que pasar el tablero, a alfa y a beta
                                                ## Colocamos -2**32 y 2**32 debido a que en teoria un numero entero tiene como
                                                ## tope 32 bits aunque sabemos que aqui en python un numero puede consumir 
                                                ## mucha mas memoria

def ganador(estado):
    ## Primero evaluaremos los posibles casos de victoria debido a que de esta forma podra ser mas claro el empate o si el juego
    ## todavia puede continuar
    ## iniciaremos por verificar las columnas y las filas
    for i in range(3):
        if  (estado[0][i] == 'o' and estado[1][i] == 'o' and estado[2][i] == 'o') or (estado[i][0] == 'o'  and estado[i][1] == 'o' and estado[i][2] == 'o'):
            ## si  gana el o entonces pasaremos un -1
            return -1
        elif (estado[0][i] == 'x' and estado[1][i] == 'x' and estado[2][i] == 'x') or (estado[i][0] == 'x'  and estado[i][1] == 'x' and estado[i][2] == 'x'):
            ## si gana el x entonces pasaremos un 1
            return 1
    ## Ahora las diagonales y pasaremos lo mismo en cada caso    
    if (estado[0][0] == 'o' and estado[1][1] == 'o' and estado[2][2] == 'o') or (estado[2][0] == 'o' and estado[1][1] == 'o' and estado[0][2] == 'o'):
        return -1
    elif (estado[0][0] == 'x' and estado[1][1] == 'x' and estado[2][2] == 'x') or (estado[2][0] == 'x' and estado[1][1] == 'x' and estado[0][2] == 'x'):
        return 1
    ## Con esto podemos verificar que en el caso de que exista algun espacio en blanco por cubrir entonces el jueog debe seguir
    for i in range(3):
        for j in range(3):
            if estado[i][j] == ' ':
                return 2
    ## En caso contrario llegamos al final del juego y todavia no existe ganador por lo cual tenemos un empate 
    return 0

def posibles_jugadas(estado, jugador):
    ## Una jugada dentro de el juego del gato se traduce a colocar tu figura correspondiente dentro de las partes no ocupadas
    ## dentro del tablero entonces necesitaremos relizar un par de operaciones
    posibles_jugadas = []
    ## Nos movmos por todo el tablero
    for i in range(3):
        for j in range(3):
            ## Si esxiste una casilla vacia
            if estado[i][j] == ' ':
                ## generamos una copia del tablero para no afectar al objeto original
                l = [estado[0][:],estado[1][:],estado[2][:]]
                ## y aporvecharemos una variable binaria antes declarada  para establecer en que turno estamos, colocamos la
                ## marca y la anexamosa las posibles jugadas
                if jugador == True:
                    l[i][j] = 'x'
                    posibles_jugadas.append(l)
                else:
                    l[i][j] = 'o'
                    posibles_jugadas.append(l)
    return posibles_jugadas

def min_jugada_a_b(estado,alfa,beta):
    gano = ganador(estado)
    if gano == 1 or gano == -1 or gano == 0:
        return gano, estado
    valor = 2**32
    for i in posibles_jugadas(estado,False):
        valor_p, estado_p = max_jugada_a_b(i,alfa,beta)
        #valor = min(valor, max_jugada)
        if valor >= valor_p:
            valor = valor_p
            estado = i
        if valor < alfa:
            return valor, estado
        beta = min(beta,valor)
    return valor, estado

def max_jugada_a_b(estado,alfa,beta):
    ## Al ser una funcion recursiva entonces necesitamos pararla de alguna forma, esta forma sera la evaluacion de ganador
    ## para ahorrar en tiempo computacional guardaremos el resultado en una variable
    gano = ganador(estado)
    if gano == 1 or gano == -1 or gano == 0:
        return gano, estado
    ## inicializamos el valor como menos infinito
    valor = -2**32
    ## calculamos las posibles jugadas de x
    for i in posibles_jugadas(estado,True):
        ## pasamos a analizar los movimientos de o, tomemos en en cuenta que el los movimientos los iremos pasando de izquierda
        ## a derecha de arriba a abajo:
        ##    1 | 2 | 3  
        ##  ------------- 
        ##   4 | 5 | 6  
        ## -------------
        ##  7 | 8 | 9  
        valor_p, estado_p = min_jugada_a_b(i,alfa,beta)
        if valor <= valor_p:
            valor = valor_p
            estado = i
        if valor > beta:
            return valor, estado
        alfa = max(alfa,valor)
    return valor, estado

def entrada_jugada(tablero):
    while 1:
        casilla = int(input())-1
        div = casilla // 3
        mod = casilla % 3
        if tablero[div][mod] == ' ':
            tablero[div][mod] = 'o'
            return tablero
        print('Movimiento no valido')
        
tablero = gato()
print('Inicia la maquina')
tablero = minimax_a_b(tablero)[1]
while ganador(tablero) == 2:
    print('  ',tablero[0][0],'|',tablero[0][1],'|',tablero[0][2],'\n','-------------','\n  ',tablero[1][0],'|',tablero[1][1], '|', tablero[1][2], '\n' , '-------------', '\n  ',tablero[2][0], '|', tablero[2][1], '|', tablero[2][2])  
    print('¡Te toca a ti!, ingresa el numero de casilla en la que quieres colocar tu "o"')
    entrada_jugada(tablero)
    tablero = minimax_a_b(tablero)[1]
res = ganador(tablero)
if res == 1:
    print('¡Gano la maquina!')
elif res == -1:
    print('¡Ganaste tu!')
elif res == 0:
    print('¡Empate!')
print('  ',tablero[0][0],'|',tablero[0][1],'|',tablero[0][2],'\n','-------------','\n  ',tablero[1][0],'|',tablero[1][1], '|', tablero[1][2], '\n' , '-------------', '\n  ',tablero[2][0], '|', tablero[2][1], '|', tablero[2][2])
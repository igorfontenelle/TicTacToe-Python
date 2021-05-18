def showBoard():
    for i in range(9):
        print(f'{board[i]} ', end='')
        if i == 2 or i == 5 or i == 8:
            print()
    print('=' * 10)

def setX():
    x = int(input('Escolha um número de 1 á 9 [X]: '))
    while True:
        for i in range(len(board)):
            if board[x - 1] == '-':
                board[x - 1] = 'X'
                break

            else:
                x = int(input('Espaço já escolhido! Tente outro número [X]: '))
        break;


def setO():
    o = int(input('Escolha um número de 1 á 9 [O]: '))
    while True:

        for i in range(len(board)):
            if board[o - 1] == '-':
                board[o - 1] = 'O'
                break
            else:
                o = int(input('Espaço já Escolhido! Tente outro número [O]: '))
        break

def checkWinnerX():
    # Verificando se X venceu pela horizontal
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
        return True
    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
        return True
    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        return True

    # Verificando se X venceu pela vertical
    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
        return True
    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        return True
    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        return True

    # Verificando se X venceu pela diagonal
    elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
        return True
    elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        return True


def checkWinnerO():
    # Verificando se X venceu pela horizontal
    if board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
        return True
    elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
        return True
    elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
        return True

    # Verificando se X venceu pela vertical
    elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
        return True
    elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
        return True
    elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        return True

    # Verificando se X venceu pela diagonal
    elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
        return True
    elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
        return True



#Programa Principal

board = ['-' for i in range(9)]
round = 1
print('------ JOGO DA VELHA ------')
showBoard()
while True:
    print(f'Round {round}')

    setX()
    showBoard()
    checkWinnerX()
    checkWinnerO()
    round += 1
    if (checkWinnerX()):
        print('Win X')
        break
    elif round >= 9:
        print('Empate')
        break
    setO()
    showBoard()
    checkWinnerX()
    checkWinnerO()
    if checkWinnerO():
        print('Win O')
        break
    elif round >= 9:
        print('Empate')
        break
    round += 1


tabuleiro = {
    7:' ', 8:' ', 9:' ',
    4:' ', 5:' ', 6:' ',
    1:' ', 2:' ', 3:' ' 
}

def clearTabuleiro():
    for k in tabuleiro:
        if tabuleiro.values() != ' ':
            tabuleiro[k] = ' '

def printTabuleiro():
    print(tabuleiro[7] + '|' + tabuleiro[8] + '|' + tabuleiro[9])
    print('-+-+-')
    print(tabuleiro[4] + '|' + tabuleiro[5] + '|' + tabuleiro[6])
    print('-+-+-')
    print(tabuleiro[1] + '|' + tabuleiro[2] + '|' + tabuleiro[3])

def game():
    p1 = 'X'
    p2 = 'O'
    count = 0

    clearTabuleiro()
    while count < 9:
        
        printTabuleiro()
        move = int(input("\n"))

        if tabuleiro[move] == ' ':
            if count%2==0:
                tabuleiro[move] = p1
                count+=1
            else:
                tabuleiro[move] = p2
                count+=1
        else:
            print('Casa indisponivel')

        if count >= 5:
            if tabuleiro[1] == tabuleiro[2] == tabuleiro[3] != ' ':
                printTabuleiro()
                print('\nGame Over')
                print('O player ' + tabuleiro[1] + ' ganhou!')
                break
            elif tabuleiro[4] == tabuleiro[5] == tabuleiro[6] != ' ':
                printTabuleiro()
                print('\nGame Over')
                print('O player ' + tabuleiro[4] + ' ganhou!')
                break
            elif tabuleiro[7] == tabuleiro[8] == tabuleiro[9] != ' ':
                printTabuleiro()
                print('\nGame Over')
                print('O player ' + tabuleiro[7] + ' ganhou!')
                break
            elif tabuleiro[1] == tabuleiro[4] == tabuleiro[7] != ' ':
                printTabuleiro()
                print('\nGame Over')
                print('O player ' + tabuleiro[1] + ' ganhou!')
                break
            elif tabuleiro[2] == tabuleiro[5] == tabuleiro[8] != ' ':
                printTabuleiro()
                print('\nGame Over')
                print('O player ' + tabuleiro[2] + ' ganhou!')
                break
            elif tabuleiro[3] == tabuleiro[6] == tabuleiro[9] != ' ':
                printTabuleiro()
                print('\nGame Over')
                print('O player ' + tabuleiro[3] + ' ganhou!')
                break
            elif tabuleiro[1] == tabuleiro[5] == tabuleiro[9] != ' ':
                printTabuleiro()
                print('\nGame Over')
                print('O player ' + tabuleiro[1] + ' ganhou!')
                break
            elif tabuleiro[3] == tabuleiro[5] == tabuleiro[7] != ' ':
                printTabuleiro()
                print('\nGame Over')
                print('O player ' + tabuleiro[3] + ' ganhou!')
                break

        if count == 9:
            print('\nGame Over')
            print('Empate!')

    resposta = input('\nVocê quer jogar novamente? (S/N)')
    if resposta == 'S':
        game()
    elif resposta == 'N':
        pass
            
game()

# JOGO NIM

def computador_escolhe_jogada(n, m):
    novonComp = 1

    while novonComp != m:
        if (n - novonComp) % (m + 1) == 0:
            return novonComp
        else:
            novonComp = novonComp + 1
    return novonComp


def usuario_escolhe_jogada(n, m):
    numeroValido = False

    while not numeroValido:
        print()
        novon = int(input("Quantas peças você vai tirar? " ))
        if novon > m or novon < 1:
            print("Oops! Jogada inválida! Tente de novo." )
        else:
            numeroValido = True
    return novon


def campeonato():
    rodada = 1
    while rodada <= 3:
        print()
        print('**** Rodada',rodada, '****')
        partida()
        rodada = rodada + 1
    placarUsu = 0
    placarComp = 3
    print()
    print("Fim do jogo! O computador ganhou!")
    print()
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você ",placarUsu,"X",placarComp,"Computador")


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    partidaComp = False

    if n % (m + 1) == 0:
        print()
        print("Você começa!")

    else:
        print()
        print("Computador começa!")
        partidaComp = True

    while n > 0:
        if partidaComp:
            novonComp = computador_escolhe_jogada(n, m)
            n = n - novonComp
            print()

            if novonComp == 1:
                print()
                print("O computador tirou uma peça")

            else:
                print()
                print("O computador tirou",novonComp,"peças" )

            partidaComp = False

        else:
           novon = usuario_escolhe_jogada(n, m)
           n = n - novon
           if novon == 1:
               print()
               print("Você tirou uma peça")

           else:
               print()
               print("Você tirou",novon,"peças" )

           partidaComp = True

        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print()
        else:
            if n!= 0:
                print("Agora restam",n, "peças no tabuleiro.")

print("Bem-vindo ao jogo do NIM! Escolha:")
print()
print("1 - para jogar uma partida isolada")
print()
print("2 - para jogar um campeonato")
escolhaPartida = int(input(" "))
print()

if escolhaPartida == 2:
    print()
    print('Voce escolheu um campeonato!')
    print()
    campeonato()
else:
    if escolhaPartida == 1:
        print()
        partida()

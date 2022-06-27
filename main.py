# Mensagem de boas vindas
import easygui as easygui
import random


def pegaraleatorio(lista):
    return random.choice(lista)


def removerdalista(lista, valor):
    return lista.remove(valor)


def decidir(valor):
    if valor == 'Rápido: 3 perguntas':
        return 1
    elif valor == 'Diverso: 10 perguntas':
        return 2
    elif valor == 'Completo: 27 perguntas':
        return 3


def jogo(listaoriginal, repeticoes):
    lista1 = listaoriginal
    lista2 = listaoriginal
    print(f'Lista 2 original: {lista2}')
    acertos = 0
    contador = 0
    ordemrespostas = []
    for x in range(repeticoes):
        contador += 1
        print(f'Rodada: {contador}')
        estado = pegaraleatorio(lista1)
        print(f'O valor de estado é: {estado}')

        print(f'Check 0 da lista2: {lista2}')

        lista2.remove(estado)

        print('-' * 200)
        print(f'Check 1 da lista2: {lista2}')
        print('-' * 200)

        listainicial = [pegaraleatorio(lista2), pegaraleatorio(lista2), estado]
        for x in range(50):
            for x in range(len(listainicial) - 1):
                if listainicial[x] == listainicial[x + 1]:
                    try:
                        lista2.remove(x)
                        listainicial.remove(listainicial[x])
                        listainicial.append(pegaraleatorio(lista2))
                        lista2.append(x)
                    except:
                        pass
                    finally:
                        pass
                else:
                    pass

        for x in range(len(listainicial) - 1):
            if listainicial[x] == estado:
                if listainicial[x + 1] == estado:
                    """
                    **************************************
                    MEXI AQUI
                    NÃO EXISTIA ESSE IF, SÓ EXISTIA O PASS
                    **************************************
                    """
                    listainicial.remove(listainicial[x])
                    listainicial.append(pegaraleatorio(lista2))
                else:
                    pass
            elif listainicial[x] == listainicial[x + 1]:
                listainicial.remove(listainicial[x])
                listainicial.append(pegaraleatorio(lista2))

        listarandom = []
        for x in range(3):
            listarandom.append(random.choice(listainicial))
            listainicial.remove(listarandom[x])

        print()
        print(f'As opções depois do shuffle são: {listarandom}')

        resposta = easygui.buttonbox(title='O jogo',
                                     image= f'C:\\Users\T-Gamer\PycharmProjects'
                                            f'\pythonProject2\Jogo\Mapas\MAPA BRASIL {estado}.png',
                                     choices=listarandom,
                                     msg=f'Rodada: {contador}')
        if resposta == estado:
            easygui.msgbox(msg='Você acertou!')
            acertos += 1
        else:
            easygui.msgbox(msg=f'Você errou. A resposta correta era {estado}')

        lista2.append(estado)

        removerdalista(lista1, estado)

        lista2.append(estado)

        ordemrespostas.append(estado)

        print(f'Check 2 da lista2: {lista2}')

    easygui.msgbox(f'Você acertou {acertos} de {repeticoes}\n'
                   f'A ordem das respotas foi {ordemrespostas}')


mapa = ['AC', 'AL', 'AM',
        'AP', 'BA', 'CE',
        'DF', 'ES', 'GO',
        'MA', 'MG', 'MS',
        'MT', 'PA', 'PB',
        'PE', 'PI', 'PR',
        'RJ', 'RN', 'RO',
        'RR', 'RS', 'SC',
        'SE', 'SP', 'TO']

# Mensagem de boas vindas
"""
easygui.msgbox(msg='Olá, seja bem vindo ao meu joguinho de Estados do Brasil.',
               title='Jogo dos Estados',
               ok_button='Vamos lá!')
"""

modo = easygui.buttonbox(msg='Qual será o modo de jogo?',
                         title='Modo de jogo',
                         choices=['Rápido: 3 perguntas',
                                  'Diverso: 10 perguntas',
                                  'Completo: 27 perguntas'])

modo = decidir(modo)

if modo == 1:
    jogo(mapa, 3)

elif modo == 2:
    jogo(mapa, 10)

elif modo == 3:
    jogo(mapa, 27)

# Mensagem de boas vindas
import easygui as easygui
import random
import os


# Pega um valor aleatório de uma lista e retorna ele como str
def pegaraleatorio(lista: list) -> str:
    return random.choice(lista)


# Remove um valor str de uma lista
def removerdalista(lista: list, valor: str) -> list:
    return lista.remove(valor)


# Mensagem inicial para escolher o modo de jogo
def inicio(facil: int, medio: int, dificil: int) -> int:
    modo = easygui.buttonbox(msg='Qual será o modo de jogo?',
                             title='Modo de jogo',
                             choices=[f'Rápido: {facil} perguntas',
                                      f'Diverso: {medio} perguntas',
                                      f'Completo: {dificil} perguntas'])
    if modo == f'Rápido: {facil} perguntas':
        jogo(mapa, facil)
    elif modo == f'Diverso: {medio} perguntas':
        jogo(mapa, medio)
    elif modo == f'Completo: {dificil} perguntas':
        jogo(mapa, dificil)


def jogo(listaoriginal: list, repeticoes: int):
    # Lista usada para o jogo escolher qual o valor da variável estado
    lista1 = listaoriginal
    """
    A ideia é que a variável lista1 só seja usada para atribuir um valor
    aleatório a variável estado, de forma que o programa não repita
    nenhuma pergunta.
    
    Ela recebe o valor inicial de mapa no início do código e depois tem
    1 valor extraído dela == ao valor de estado no final do loop de
    repetição.
    """

    # Lista usada para escolher 2 valores aleatórios
    lista2 = listaoriginal
    """
    A ideia é que a variável lista2 seja usada para extrair 2 valores
    aleatórios que serão usados para formar as 2 respostas erradas do
    jogo.
    
    Marcado em "*1-"
    Ela recebe o valor inicial de mapa no início do código e em seguida
    tem o valor de estado extraído dela, para que as duas opções
    erradas não sejam iguais à opção correta. No final do loop, o valor
    de estado é adicionado ao final da lista2 com a função append().
    """
    # Contador de acertos
    acertos = 0
    # Contador da rodada
    contador = 0
    # Mostra qual foi a ordem correta das respostas no final do jogo
    ordemrespostas = []

    # Identifica o diretório no qual o arquivo "main.py" está
    abspath = os.path.abspath(__file__)
    local1 = os.path.dirname(abspath)
    """
    Usado para que o programa consiga identificar o diretório em que ele
    está, permitindo que ele consiga acessar os arquivos .png dos mapas.
    
    Permite que o diretório "Jogo-dos-Estados" possa ser realocado dentro
    da máquina sem que ocorra conflito dentro do código.
    """

    # Repete com base na escolha do modo de jogo
    for x in range(repeticoes):
        contador += 1
        print(f'Rodada: {contador}')
        estado = pegaraleatorio(lista1)
        print(f'O valor de estado é: {estado}')

        # Dentro do loop para que seja atualizada com o próximo diretório após cada loop
        local2 = f"""{local1}\\Mapas\\MAPA BRASIL {estado}.png"""

        # *1 - Variável estado removida de lista2 para que o valor correto não seja escolhido
        lista2.remove(estado)
        # É criada uma lista contendo 2 valores aleatórios e 1 valor == estado
        listainicial = [pegaraleatorio(lista=lista2), pegaraleatorio(lista=lista2), estado]

        # Testa se as opções não se repetiram
        """
        # Teste meia boca
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
            """

        # Teste bom
        for z in range(50):
            for y in range(len(listainicial) - 1):
                if listainicial[y] == estado:
                    if listainicial[y + 1] == estado:
                        listainicial.remove(listainicial[y])
                        listainicial.append(pegaraleatorio(lista=lista2))
                    else:
                        pass
                elif listainicial[y] == listainicial[y + 1]:
                    listainicial.remove(listainicial[y])
                    listainicial.append(pegaraleatorio(lista=lista2))

        listarandom = []
        for a in range(3):
            listarandom.append(random.choice(listainicial))
            listainicial.remove(listarandom[a])

        print(f'As opções são: {listarandom}')

        resposta = easygui.buttonbox(title='O jogo',
                                     image=local2,
                                     choices=listarandom,
                                     msg=f'Rodada: {contador}')
        if resposta == estado:
            easygui.msgbox(msg='Você acertou!')
            acertos += 1
        else:
            easygui.msgbox(msg=f'Você errou. A resposta correta era {estado}')
            pass

        lista2.append(estado)

        removerdalista(lista=lista1, valor=estado)

        lista2.append(estado)

        ordemrespostas.append(estado)

    # Mensagem final
    easygui.msgbox(msg=f'Você acertou {acertos} de {repeticoes}\n'
                   f'A ordem das respotas foi {ordemrespostas}',
                   title='Resultado',
                   ok_button='Encerrar')
    print(f'A ordem das respotas foi {ordemrespostas}')


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

if __name__ == '__main__':
    inicio(3, 10, 27)

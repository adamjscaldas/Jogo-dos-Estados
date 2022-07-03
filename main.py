import easygui
import random
import os


# Pega um valor aleatório de uma lista e retorna ele como str
def pegaraleatorio(lista: list) -> str:
    return random.choice(lista)


# Remove um valor str de uma lista
def removerdalista(lista: list, valor: str):
    lista.remove(valor)


# Função que inicia o jogo
def inicio():
    """
    O if serve para que, caso o usuário feche a janela do jogo, o
    programa encerre, sem que ocorram erros.

    Se o usuário escolher a opção "Info" o valor retornado será 0,
    esse while faz com que, sempre que a pessoa fechar a janela que
    "Info" abre, o código retorne para a seleção de dificuldade

    :return:
    """
    modo = escolher()
    modo = conversor(modo=modo)
    modo = loop(dificuldade=modo)
    if modo is None:
        pass
    while modo == 0:
        modo = escolher()
        modo = conversor(modo)
        modo = loop(dificuldade=modo)


def escolher(facil=3, medio=10, dificil=27) -> str:
    """
    Imprime uma janela com botões para escolher o modo de jogo. Também
    permite que o usuário abra uma janela para criar uma partida
    customizada, ou uma janela com informações sobre o jogo.

    :param facil:
    :param medio:
    :param dificil:
    :return:
    """
    return easygui.buttonbox(msg='Qual será o modo de jogo?',
                             title='Modo de jogo',
                             choices=[f'Rápido: {facil} perguntas',
                                      f'Diverso: {medio} perguntas',
                                      f'Completo: {dificil} perguntas',
                                      f'Custom',
                                      f'Info'])


def custom():
    """
    Imprime uma janela na qual o usuário pode digitar a quantidade de
    partidas que o jogo terá e escolher se as respostas vão se repetir
    ou não.

    :return:
    """
    return easygui.multenterbox(msg='Aqui você pode criar uma partida customizada.\n\n'
                                    'Defina o número de rodadas que o jogo terá e se os Estados '
                                    'poderão ou não se repetir.\n\n'
                                    '0 = Não repete\n1 = Repete\n\n'
                                    'Se você configurar a partida para ter mais de 27 rodadas, '
                                    'o jogo se configurará para que as repostas se repitam.',
                                title='Partida customizada',
                                fields=['Rodadas', 'Repetir Estados'],
                                values=['10', '1'])


def conversor(modo: str, facil=3, medio=10, dificil=27) -> str:
    """
    Converte a str que a função escolher() retorna para um valor
    mais compacto.

    :param modo:
    :param facil:
    :param medio:
    :param dificil:
    :return:
    """
    if modo == f'Rápido: {facil} perguntas':
        return 'FACIL'
    elif modo == f'Diverso: {medio} perguntas':
        return 'MEDIO'
    elif modo == f'Completo: {dificil} perguntas':
        return 'DIFICIL'
    elif modo == "Info":
        return 'INFO'
    elif modo == 'Custom':
        return 'CUSTOM'
    else:
        return 'QUIT'


def loop(dificuldade: str, facil=3, medio=10, dificil=27):
    """
    Com base no valor retornado por conversor(), determina qual ação
    o código tomará.

    Se conversor() retornar 'FACIL', 'MEDIO' ou 'DIFICIL', o código
    inicia o jogo com base na dificuldade que estiver definida para
    cada modo.

    Se conversor() retornar 'INFO' ou 'CUSTOM', abre uma janela
    com informações sobre o jogo ou uma tela para fazer um jogo
    com uma quantidade customizada de perguntas, respectivamente.

    :param dificuldade:
    :param facil:
    :param medio:
    :param dificil:
    :return:
    """
    if dificuldade.upper() == 'FACIL':
        jogo1(listaoriginal=mapa, repeticoes=facil, random=0)
    elif dificuldade.upper() == 'MEDIO':
        jogo1(listaoriginal=mapa, repeticoes=medio, random=0)
    elif dificuldade.upper() == 'DIFICIL':
        jogo1(listaoriginal=mapa, repeticoes=dificil, random=0)
    elif dificuldade.upper() == 'INFO':
        retornar = easygui.msgbox(msg='Este é o Jogo dos Estados feito por Adam Johannes.\n\n'
                                      'A proposta do jogo é acertar o maior número de '
                                      'Estados que você conseguir.\n\n'
                                      'Ao escolher um modo de jogo, uma imagem aparecerá na '
                                      'sua tela e logo abaixo dela haverão três opções, uma '
                                      'correta e duas incorretas.\n\n'
                                      'Por padrão, o jogo não irá repetir os Estados que aparecem, '
                                      'porém, é possível criar uma partida customizada através da '
                                      'opção "Custom" onde as respostas podem se repetir.'
                                      '\n\n'
                                      'Boa sorte!',
                                  title='Informações',
                                  ok_button='Retornar')
        if retornar == "Retornar":
            return 0
        else:
            return 0
    elif dificuldade.upper() == 'CUSTOM':
        valores = custom()
        saida = 0
        repeticoes = 0
        repetir = 0
        # Tem que transformar em um ciclo de testagem para que só possa ser int
        while saida == 0:
            if valores is None:
                return 0
            else:
                try:
                    repeticoes = int(valores[0])
                    repetir = int(valores[1])
                    saida = 1
                    if repeticoes > 27:
                        repetir = 1
                except:
                    valores = custom()
                finally:
                    pass
        jogo1(listaoriginal=mapa, repeticoes=repeticoes, random=repetir)
    elif dificuldade.upper() == 'QUIT':
        return None


def testar(lista_teste: list, lista_extrair: list, valor: str) -> list:
    """
    Testa se os valores de uma lista não estão repetidos.

    :param lista_teste:
    :param lista_extrair:
    :param valor:
    :return:
    """
    for z in range(50):
        for y in range(len(lista_teste) - 1):
            if lista_teste[y] == valor:
                if lista_teste[y + 1] == valor:
                    lista_teste.remove(lista_teste[y])
                    lista_teste.append(pegaraleatorio(lista=lista_extrair))
                else:
                    pass
            elif lista_teste[y] == lista_teste[y + 1]:
                lista_teste.remove(lista_teste[y])
                lista_teste.append(pegaraleatorio(lista=lista_extrair))
    return lista_teste


def randomizar(lista_input: list, lista_output: list) -> list:
    """
    Coloca os elementos de uma lista em uma ordem aleatória.

    :param lista_input:
    :param lista_output:
    :return:
    """
    for a in range(3):
        lista_output.append(random.choice(lista_input))
        lista_input.remove(lista_output[a])
    return lista_output


def respostas(imagem: str, escolhas: list, contador: int) -> str:
    """
    Imprime uma janela com uma imagem e botões com respostas.
    :param imagem:
    :param escolhas:
    :param contador:
    :return:
    """
    while True:
        valor = easygui.buttonbox(title='O jogo',
                                  image=imagem,
                                  choices=escolhas,
                                  msg=f'Rodada: {contador}',
                                  cancel_choice='X')
        if valor != imagem:
            return valor
        else:
            pass


def certo_errado(resposta: str, estado: str, acertos: int):
    """
    Verifica se a resposta selecionada corresponde com a imagem/valor
    da variável estado que armazena a resposta correta.

    :param resposta:
    :param estado:
    :param acertos:
    :return:
    """
    if resposta == estado:
        easygui.msgbox(msg='Você acertou!')
        resultado = acertos + 1
        return resultado
    else:
        easygui.msgbox(msg=f'Você errou. A resposta correta era {estado}')
        pass


def jogo1(listaoriginal: list, repeticoes: int, random=0):
    """
    Define as variáveis iniciais do código e testa se o usuário
    escolheu jogar um jogo onde as respostas podem ou não repetir.

    :param listaoriginal:
    :param repeticoes:
    :param random:
    :return:
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
    if random == 0:
        print('Nessa partida, os Estados não vão se repetir')
        # Lista usada para o jogo escolher qual o valor da variável estado
        lista1 = []
        lista1 += listaoriginal
        """
        A ideia é que a variável lista1 só seja usada para atribuir um valor
        aleatório a variável estado, de forma que o programa não repita
        nenhuma pergunta.
        
        Ela recebe o valor inicial de mapa no início do código e depois tem
        1 valor extraído dela == ao valor de estado no final do loop de
        repetição.
        """

        # Lista usada para escolher 2 valores aleatórios
        lista2 = []
        lista2 += listaoriginal
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
        jogo2(lista1=lista1,
              lista2=lista2,
              contador=contador,
              ordemrespostas=ordemrespostas,
              local1=local1,
              repeticoess=repeticoes,
              acertoss=acertos)

    elif random == 1:
        print('Nessa partida, os Estados podem se repetir')
        lista1 = listaoriginal
        lista2 = listaoriginal
        jogo2(lista1=lista1,
              lista2=lista2,
              contador=contador,
              ordemrespostas=ordemrespostas,
              local1=local1,
              repeticoess=repeticoes,
              acertoss=acertos)


def jogo2(lista1: list,
          lista2: list,
          contador: int,
          ordemrespostas: list,
          local1: str,
          repeticoess: int,
          acertoss: int):
    """
    Função que roda o jogo, realizando as repetições com base na
    quantidade de rodadas selecionada. Dentro dela, quase todas
    as funções anteriores estão incluídas.

    :param lista1:
    :param lista2:
    :param contador:
    :param ordemrespostas:
    :param local1:
    :param repeticoess:
    :param acertoss:
    :return:
    """
    # Repete com base na escolha do modo de jogo
    for x in range(repeticoess):
        contador += 1
        estado = pegaraleatorio(lista=lista1)

        # Dentro do loop para que seja atualizada com o próximo diretório após cada loop
        local2 = f"""{local1}\\Mapas\\MAPA BRASIL {estado}.png"""

        # *1 - Variável estado removida de lista2 para que o valor correto não seja escolhido
        lista2.remove(estado)
        # É criada uma lista contendo 2 valores aleatórios e 1 valor == estado
        listainicial = [pegaraleatorio(lista=lista2), pegaraleatorio(lista=lista2), estado]

        # Testa se as opções não se repetiram
        listainicial = testar(lista_teste=listainicial, lista_extrair=lista2, valor=estado)

        # Faz com que a ordem da lista seja aleatória
        listarandom = []
        listarandom = randomizar(lista_input=listainicial, lista_output=listarandom)

        # Imprime uma caixa com o mapa, 2 respostas erradas e uma correta
        """
        Se o usuário não selecionar nenhuma das 3 opções com valores dos Estados, entra em
        um loop que imprime a caixa até uma das 3 respostas ser selecionada
        """
        resposta = respostas(imagem=local2, escolhas=listarandom, contador=contador)

        while resposta not in listarandom:
            resposta = respostas(imagem=local2, escolhas=listarandom, contador=contador)

        acertos = certo_errado(resposta=resposta, estado=estado, acertos=acertoss)
        lista2.append(estado)

        # Remove o valor estado da lista1
        removerdalista(lista=lista1, valor=estado)

        lista2.append(estado)

        ordemrespostas.append(estado)

    # Mensagem final
    easygui.msgbox(msg=f'Você acertou {acertoss} de {repeticoess}\n'
                       f'A ordem das respotas foi {ordemrespostas}',
                   title='Resultado',
                   ok_button='Encerrar')
    print(f'A ordem das respotas foi {ordemrespostas}')


if __name__ == '__main__':
    # Lista com todos os 27 Estados
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
    easygui.msgbox(msg='Olá, seja bem vindo ao jogo dos Estados do Brasil!',
                   title='Jogo dos Estados',
                   ok_button='Vamos lá!')
    # Inicia o jogo
    inicio()

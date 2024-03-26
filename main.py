candidatos = [
    ('João','e5_t10_p8_s8'),
    ('José','e10_t7_p7_s8'),
    ('Marcos','e8_t5_p4_s9'),
    ('Marlon','e2_t2_p2_s1'),
    ('Alex','e10_t10_p8_s9')
]
#função para inserir novos candidatos e suas notas
def inserir_dados():
    while True:

        nome_candidato = input('insira o nome do candidato: ')

        e = input("insira a nota de entrevista: ")
        t = input("insira a nota do teste teórico: ")
        p = input("insira a nota do teste prático: ")
        s = input("insira a nota de soft skills: ")

        texto_nota = f'e{e}_t{t}_p{p}_s{s}'
        tupla_nota_candidato = (nome_candidato,texto_nota)
        candidatos.append(tupla_nota_candidato)

        again = input('Deseja inserir un novo candidato? (s ou n)')
        if again == 'n':
            break
    return candidatos
#Função para achar candidatos de acordo com as notas de corte selecionadas
def achar_candidato(candidatos):
    print()

    nota_esperadas = []
    nota_e = int(input('insira a nota esperada na entrevista: '))
    nota_t = int(input('insira a nota esperada no teste teórico: '))
    nota_p = int(input('insira a nota esperada no teste prático: '))
    nota_s = int(input('insira a nota esperada na avaliação de soft skills: '))

    nota_esperadas.append(nota_e)
    nota_esperadas.append(nota_t)
    nota_esperadas.append(nota_p)
    nota_esperadas.append(nota_s)

    dicionario_notas = {}
    for candidato, notas_str in candidatos:
        dicionario_notas[candidato] = converter_notas(notas_str)

    lista_aptos = []

    for candidato, valor in dicionario_notas.items():
        nota_esperada = 0
        if valor['e'] >= nota_esperadas[0]:
            nota_esperada += 1
        if valor['t'] >= nota_esperadas[1]:
            nota_esperada += 1
        if valor['p'] >= nota_esperadas[2]:
            nota_esperada += 1
        if valor['s'] >= nota_esperadas[3]:
            nota_esperada += 1
        if nota_esperada == 4:
            lista_aptos.append(candidato)

    candidatos_string = ""

    for candidato in lista_aptos:
        candidatos_string += candidato + ", "

    #Remover a vírgula e o espaço extras do final da string
    candidatos_string = candidatos_string[:-2]

    # Verifica se há apenas um candidato
    if len(lista_aptos) == 1:
        mensagem = 'O candidato que passou na prova: '
    elif len(lista_aptos)>1:
        mensagem = 'Candidatos que passaram na prova: '
    else:
        mensagem = 'Nenhum candidato apto'


    
    return print(mensagem,candidatos_string)

#Função para converter a string de notas em um dicionário
def converter_notas(nota_str):
    notas_dict = {}
    notas_str_split = nota_str.split('_')
    for item in notas_str_split:
        notas_dict[item[0]] = int(item[1:])
    return notas_dict


#Inserir novos candidatos e suas notas
primeira_vez = True
while True:
    if primeira_vez:
        opcao = input("""
        Bem vindo a Consulta, inserção de dados ou seleção de candidatos aptos a uma nota que você preferir
        O que deseja fazer?
        1 - Inserir um novo candidato
        2 - Selecionar candidato a partir de notas definidas por você
        3 - Consultar lista de candidatos
        4 - Fechar Programa
        """)
    primeira_vez = False

    if opcao == '1':
        print('Você Deseja cadastrar um candidato ')
        inserir_dados()
    if opcao == '2':
        print('Você Deseja selecionar um candidato ')
        achar_candidato(candidatos)

    if opcao == '3':
        print('Lista de candidados e suas notas')
        print(candidatos)

    if opcao == '4':
        break

    opcao = input("""
        O que deseja fazer?
        1 - Inserir um novo candidato
        2 - Selecionar candidato a partir de notas definidas por você
        3 - Consultar lista de candidatos
        4 - Fechar Programa
        """)




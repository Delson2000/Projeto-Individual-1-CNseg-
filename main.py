candidatos = [
    ('candidato 1','e5_t10_p8_s8'),
    ('candidato 2','e10_t7_p7_s8'),
    ('candidato 3','e8_t5_p4_s9'),
    ('candidato 4','e2_t2_p2_s1'),
    ('candidato 5','e10_t10_p8_s9')
]
#função para inserir novos candidatos e suas notas
def inserir_dados():
    while True:
        again = input('Deseja inserir un novo candidato? (s ou n)')
        if again == 'n':
            break

        nome_candidato = input('insira o nome do candidato: ')

        e = input("insira a nota de entrevista: ")
        t = input("insira a nota do teste teórico: ")
        p = input("insira a nota do teste prático: ")
        s = input("insira a nota de soft skills: ")

        texto_nota = f'e{e}_t{t}_p{p}_s{s}'
        tupla_nota_candidato = (nome_candidato,texto_nota)
        candidatos.append(tupla_nota_candidato)
    # print(candidatos)
    return candidatos
#Função para achar candidatos de acordo com as notas de corte selecionadas
def achar_candidato(dict_notas):

    nota_esperadas = []
    nota_e = int(input('insira a nota esperada na entrevista: '))
    nota_t = int(input('insira a nota esperada no teste teórico: '))
    nota_p = int(input('insira a nota esperada no teste prático: '))
    nota_s = int(input('insira a nota esperada na avaliação de soft skills: '))

    nota_esperadas.append(nota_e)
    nota_esperadas.append(nota_t)
    nota_esperadas.append(nota_p)
    nota_esperadas.append(nota_s)

    lista_aptos = []

    for candidato, valor in dict_notas.items():
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
    
    return lista_aptos

#Função para converter a string de notas em um dicionário
def converter_notas(nota_str):
    notas_dict = {}
    notas_str_split = nota_str.split('_')
    for item in notas_str_split:
        notas_dict[item[0]] = int(item[1:])
    return notas_dict


#Inserir novos candidatos e suas notas
inserir_dados()

#Criar o dicionário de notas
dicionario_notas = {}
for candidato, notas_str in candidatos:
    dicionario_notas[candidato] = converter_notas(notas_str)

#Visualizar o dicionario de notas    
print(dicionario_notas)

print(dicionario_notas['candidato 2']['e'])

aptos = achar_candidato(dicionario_notas)

candidatos_string = ""

for candidato in aptos:
    candidatos_string += candidato + ", "

#Remover a vírgula e o espaço extras do final da string
candidatos_string = candidatos_string[:-2]

print('Os candidatos que foram passaram nas provas foram: ',candidatos_string)
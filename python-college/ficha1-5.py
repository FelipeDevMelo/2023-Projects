##################      Slide 1     ##############################

# questao 1 #########################

# palavras = ["manga", "banana", "ovo", "ovo", "amor", "roma"]
# paresInvertidos = []
# for i in range(len(palavras)):
#     for j in range(i+1, len(palavras)):
#         if palavras[i][::-1] == palavras[j]:
#             paresInvertidos.append((palavras[i], palavras[j]))

# print("pares invertidos:\n", paresInvertidos)


# questao 2#########################

# import random

# dados = []
# faces = [0, 0, 0, 0, 0, 0]
# for i in range(50):
#     dados.append(random.randint(1, 6))
#     for j in range(6):
#         if j+1 == dados[i]:
#             faces[j] += 1

# print("porcentagem dos lados:")
# for i in range(6):
#     porcentagem = round((faces[i]/50)*100,2)
#     print(i+1," : ",porcentagem,"%")

# questao 3 #########################

# string1 = input("informe a primeira string")
# string2 = input("informe a segunda string")

# if string1 == string2:
#     print(" as duas tem o mesmo conteudo e tem o mesmo comprimento")


# else:
#     print("as duas tem conteudos diferentes")
#     if len(string1) == len(string2):
#         print("e tem o mesmo comprimento")





# questao 4#########################
# agenda = {}

# def incluir_novo_nome():
#     nome = input("Digite o nome da pessoa que deseja incluir na agenda: ")
#     telefones = input("Digite o(s) telefone(s) da pessoa separados por vírgula: ")
#     telefones = [telefone.strip() for telefone in telefones.split(",")]
#     agenda[nome] = telefones
#     print(f"{nome} adicionado(a) na agenda com o(s) telefone(s): {telefones}")

# def incluir_telefone():
#     nome = input("Digite o nome da pessoa que deseja adicionar um telefone: ")
#     if nome not in agenda:
#         incluir = input(f"{nome} não encontrado(a) na agenda. Deseja incluí-lo(a) na agenda? (S/N): ")
#         if incluir.upper() == "S":
#             incluir_novo_nome()
#             return
#         else:
#             return
#     telefone = input("Digite o telefone que deseja adicionar: ")
#     agenda[nome].append(telefone)
#     print(f"Telefone {telefone} adicionado para {nome}")

# def excluir_telefone():
#     nome = input("Digite o nome da pessoa que deseja excluir um telefone: ")
#     if nome not in agenda:
#         print(f"{nome} não encontrado(a) na agenda")
#         return
#     if len(agenda[nome]) == 1:
#         excluir_nome()
#         return
#     telefone = input("Digite o telefone que deseja excluir: ")
#     if telefone not in agenda[nome]:
#         print(f"{telefone} não encontrado para {nome}")
#         return
#     agenda[nome].remove(telefone)
#     print(f"Telefone {telefone} excluído para {nome}")

# def excluir_nome():
#     nome = input("Digite o nome da pessoa que deseja excluir: ")
#     if nome not in agenda:
#         print(f"{nome} não encontrado(a) na agenda")
#         return
#     del agenda[nome]
#     print(f"{nome} excluído(a) da agenda")

# def consultar_telefone():
#     nome = input("Digite o nome da pessoa que deseja consultar o telefone: ")
#     if nome not in agenda:
#         print(f"{nome} não encontrado(a) na agenda")
#         return
#     telefones = ", ".join(agenda[nome])
#     print(f"Telefones de {nome}: {telefones}")

# def menu():
#     while True:
#         print("\nAGENDA TELEFÔNICA\n")
#         print("Selecione uma opção:")
#         print("1 - Incluir novo nome")
#         print("2 - Incluir telefone")
#         print("3 - Excluir telefone")
#         print("4 - Excluir nome")
#         print("5 - Consultar telefone")
#         print("0 - Sair")
#         opcao = input("Opção: ")
#         if opcao == "1":
#             incluir_novo_nome()
#         elif opcao == "2":
#             incluir_telefone()
#         elif opcao == "3":
#             excluir_telefone()
#         elif opcao == "4":
#             excluir_nome()
#         elif opcao == "5":
#             consultar_telefone()
#         elif opcao == "0":
#             break
#         else:
#             print("Opção inválida")

# menu()

##################      Slide 2     ##############################

#questao 1 

# horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
# valor_hora = float(input("Digite o valor da hora de trabalho: "))

# salario_mensal = horas_trabalhadas * valor_hora

# print(f"O salário mensal é de R$ {salario_mensal:.2f}")


#questao 2

# horas = int(input("Digite o número de horas de prova: "))
# minutos = int(input("Digite o número de minutos de prova: "))

# tempo_total_minutos = horas * 60 + minutos
# tempo_total_segundos = tempo_total_minutos * 60

# print(f"O tempo total de prova foi de {tempo_total_minutos} minutos, ou {tempo_total_segundos} segundos.")

#questao 3


# metros = float(input("Digite um valor em metros: "))

# centimetros = metros * 100

# print(f"{metros} metros correspondem a {centimetros} centímetros.")


#questao 4


# nota1 = float(input("Digite a primeira nota bimestral: "))
# nota2 = float(input("Digite a segunda nota bimestral: "))
# nota3 = float(input("Digite a terceira nota bimestral: "))
# nota4 = float(input("Digite a quarta nota bimestral: "))

# media = (nota1 + nota2 + nota3 + nota4) / 4

# print(f"A média das notas bimestrais é {media:.2f}.")


#questao 5

# import math

# raio = 5
# area = math.pi * raio ** 2

# print(f"A área do círculo é {area:.2f} cm².")


#questao 6

# lado = float(input("Digite o tamanho do lado do quadrado: "))

# area = lado ** 2
# dobro_area = 2 * area

# print(f"A área do quadrado é {area:.2f} e o dobro da área é {dobro_area:.2f}.")

#questao 7

# idades = [10, 12, 15, 17]
# nova_idade = 16

# media_idade = sum(idades) / len(idades)
# print(f"A média de idade do grupo é {media_idade:.2f} anos.")

# idades.append(nova_idade)
# nova_media = sum(idades) / len(idades)
# variacao_percentual = (nova_media - media_idade) / media_idade * 100
# print(f"A nova média de idade do grupo é {nova_media:.2f} anos, com uma variação percentual de {variacao_percentual:.2f}% em relação à média anterior.")

#questao 8

# temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

# temp_celsius = (temp_fahrenheit - 32) * 5/9

# print(f"A temperatura em Celsius é {temp_celsius:.2f} graus.")


#questao 9

# lado = float(input("Digite o valor do lado do quadrado: "))

# area = lado ** 2

# print(f"A área do quadrado é {area:.2f}.")

#questao 10

# base = float(input("Digite o valor da base do triângulo: "))
# altura = float(input("Digite o valor da altura do triângulo: "))

# area = (base * altura) / 2

# print(f"A área do triângulo é {area:.2f}.")

#questao 11 

# import math

# raio = float(input("Digite o valor do raio do círculo: "))
# pi = math.pi

# area = pi * (raio ** 2)
# perimetro = 2 * pi * raio
# diametro = 2 * raio

# print(f"A área do círculo é {area:.2f}.")
# print(f"O perímetro do círculo é {perimetro:.2f}.")
# print(f"O diâmetro do círculo é {diametro:.2f}.")


#questao 12

# import math

# area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

# litros = math.ceil(area / 3)  # arredonda para cima para garantir que terá tinta suficiente
# latas = math.ceil(litros / 18)  # arredonda para cima para garantir que terá latas suficientes
# preco = latas * 80

# print(f"Serão necessárias {latas} latas de tinta, com um preço total de R${preco:.2f}.")

#questao 13

# # pede dois números inteiros e um número real
# num1 = int(input("Digite o primeiro número inteiro: "))
# num2 = int(input("Digite o segundo número inteiro: "))
# num3 = float(input("Digite o número real: "))

# # calcula o produto do dobro do primeiro com metade do segundo
# prod = 2 * num1 * (num2 / 2)

# # calcula a soma do triplo do primeiro com o terceiro
# soma = 3 * num1 + num3

# # calcula o terceiro elevado ao cubo
# cubo = num3 ** 3

# # imprime os resultados
# print("O produto do dobro do primeiro com metade do segundo é:", prod)
# print("A soma do triplo do primeiro com o terceiro é:", soma)
# print("O terceiro elevado ao cubo é:", cubo)

##################      Slide 3    ##############################

#questao 1

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# num3 = int(input("Digite o terceiro número: "))

# maior = num1
# if num2 > maior:
#     maior = num2
# if num3 > maior:
#     maior = num3

# menor = num1
# if num2 < menor:
#     menor = num2
# if num3 < menor:
#     menor = num3

# print("O maior número é:", maior)
# print("O menor número é:", menor)

#questao 2


## pedindo os três valores distintos para o usuário
# num1 = int(input("Digite o primeiro valor: "))
# num2 = int(input("Digite o segundo valor: "))
# num3 = int(input("Digite o terceiro valor: "))

# # criando a lista de valores ordenados
# ordenados = []

# # verificando qual é o menor valor entre os três e adicionando na lista de ordenados
# if num1 <= num2 and num1 <= num3:
#     ordenados.append(num1)
#     if num2 <= num3:
#         ordenados.append(num2)
#         ordenados.append(num3)
#     else:
#         ordenados.append(num3)
#         ordenados.append(num2)
# elif num2 <= num1 and num2 <= num3:
#     ordenados.append(num2)
#     if num1 <= num3:
#         ordenados.append(num1)
#         ordenados.append(num3)
#     else:
#         ordenados.append(num3)
#         ordenados.append(num1)
# else:
#     ordenados.append(num3)
#     if num1 <= num2:
#         ordenados.append(num1)
#         ordenados.append(num2)
#     else:
#         ordenados.append(num2)
#         ordenados.append(num1)

# # exibindo os valores ordenados
# print("Valores ordenados em ordem crescente: ", ordenados)

#questao 3

# idade = int(input("Digite a idade do nadador: "))

# if idade >= 5 and idade <= 7:
#     categoria = "Infantil A"
# elif idade >= 8 and idade <= 10:
#     categoria = "Infantil B"
# elif idade >= 11 and idade <= 13:
#     categoria = "Juvenil A"
# elif idade >= 14 and idade <= 17:
#     categoria = "Juvenil B"
# else:
#     categoria = "Adulto"

# print("O nadador se enquadra na categoria:", categoria)


#questao 4

# numero = int(input("Digite um número inteiro: "))

# # Verifica se o número é par ou ímpar
# if numero % 2 == 0:
#     print("O número é par.")
# else:
#     print("O número é ímpar.")

# # Verifica se o número é positivo ou negativo
# if numero > 0:
#     print("O número é positivo.")
# elif numero < 0:
#     print("O número é negativo.")
# else:
#     print("O número é zero.")

#questao 5

# # leitura do salário e código do cargo
# salario = float(input("Digite o salário do funcionário: "))
# codigo = int(input("Digite o código do cargo do funcionário: "))

# # cálculo do novo salário de acordo com o cargo
# if codigo == 310:
#     novo_salario = salario * 0.05
# elif codigo == 456:
#     novo_salario = salario * 0.075
# elif codigo == 885:
#     novo_salario = salario * 0.1
# else:
#     novo_salario = salario * 0.15

# # exibição do salário antigo, novo salário e diferença
# print(f"Salário antigo: R$ {salario:.2f}")
# print(f"Novo salário: R$ {novo_salario:.2f}")
# print(f"Diferença: R$ {novo_salario - salario:.2f}")



##################      Slide 4    ##############################

#questao 1

# for i in range(51):
#     print(i)

#questao 2

# for num in range(51):
#     if num % 2 == 0:
#         print(num)


#questao 3

# inicio = int(input("Digite o número inicial: "))
# fim = int(input("Digite o número final: "))

# contagem = 0

# for num in range(inicio, fim+1):
#     if num % 2 == 0:
#         contagem += 1

# print("A quantidade de números pares entre", inicio, "e", fim, "é:", contagem)

#questao 4

# numero = int(input("Digite um número inteiro: "))

# fatorial = 1

# if numero < 0:
#     print("O fatorial de números negativos não é definido!")
# elif numero == 0:
#     print("O fatorial de 0 é 1")
# else:
#     for i in range(1, numero+1):
#         fatorial *= i

#     print("O fatorial de", numero, "é", fatorial)

#questao 5


# base = int(input("Digite a base: "))
# expoente = int(input("Digite o expoente: "))

# potencia = 1

# for i in range(expoente):
#     potencia *= base

# print(base, "elevado a", expoente, "é igual a", potencia)

#questao 6


# num = int(input("Digite um número entre 1 e 10: "))

# print("Tabuada do", num, ":")

# for i in range(1, 11):
#     print(num, "x", i, "=", num*i)

#questao 7

# num = int(input("Digite um número inteiro: "))
# soma = 0

# for i in range(1, num):
#     if num % i == 0:
#         soma += i

# print("A soma dos divisores de", num, "é", soma)

#questao 8

# n = int(input("Digite um número inteiro e positivo: "))
# soma = 0

# for i in range(1, n+1):
#     soma += 1/i

# print("O número harmônico de", n, "é", soma)

#questao 9

# n = int(input("Digite o número de termos da série de Fibonacci: "))

# a, b = 1, 1
# print(a)
# print(b)

# for i in range(n-2):
#     c = a + b
#     print(c)
#     a = b
#     b = c


#questao 10

# a, b = 1, 1
# print(a)
# print(b)

# while b <= 500:
#     c = a + b
#     print(c)
#     a = b
#     b = c


#questao 11

# n = int(input("Digite um número inteiro para calcular o fatorial: "))
# fat = 1

# for i in range(2, n+1):
#     fat *= i

# print(n, "! =", fat)



#questao 12


# num_habitantes = int(input("Digite o número de habitantes da cidade: "))

# soma_salarios = 0
# soma_filhos = 0
# maior_salario = 0
# count_salario_menor_150 = 0

# for i in range(num_habitantes):
#     salario = float(input("Digite o salário do habitante {}: ".format(i+1)))
#     num_filhos = int(input("Digite o número de filhos do habitante {}: ".format(i+1)))

#     soma_salarios += salario
#     soma_filhos += num_filhos
#     if salario > maior_salario:
#         maior_salario = salario
#     if salario < 150:
#         count_salario_menor_150 += 1

# media_salarios = soma_salarios / num_habitantes
# media_filhos = soma_filhos / num_habitantes
# percentual_salario_menor_150 = (count_salario_menor_150 / num_habitantes) * 100

# print("Média de salário: R$ {:.2f}".format(media_salarios))
# print("Média de filhos: {:.2f}".format(media_filhos))
# print("Maior salário: R$ {:.2f}".format(maior_salario))
# print("Percentual de pessoas com salário menor que R$150,00: {:.2f}%".format(percentual_salario_menor_150))



##################      Slide 5   ##############################

#questao 1


# Lê as duas strings
# string1 = input("Digite a primeira string: ")
# string2 = input("Digite a segunda string: ")

# # Informa o conteúdo das strings e seus comprimentos
# print("Conteúdo da primeira string: " + string1)
# print("Comprimento da primeira string: " + str(len(string1)))
# print("Conteúdo da segunda string: " + string2)
# print("Comprimento da segunda string: " + str(len(string2)))

# # Verifica se as strings possuem o mesmo comprimento
# if len(string1) == len(string2):
#     print("As strings possuem o mesmo comprimento")
# else:
#     print("As strings possuem comprimentos diferentes")

# # Verifica se as strings possuem o mesmo conteúdo
# if string1 == string2:
#     print("As strings possuem o mesmo conteúdo")
# else:
#     print("As strings possuem conteúdos diferentes")


#questao 2

# # Lê o nome do usuário
# nome = input("Digite seu nome: ")

# # Converte o nome para letras maiúsculas e o exibe de trás para frente
# print("Seu nome de trás para frente é:", nome.upper()[::-1])


#questao 3

# # Solicita uma string ao usuário
# string = input("Digite uma string: ")

# # Itera pela string e imprime a escada
# for i in range(len(string)):
#     print(string[:i+1])

#questao 4

# palavra = input("Digite uma palavra: ")

# for i in range(len(palavra), 0, -1):
#     espacos = " " * (i - 1)
#     print(espacos + palavra[:len(palavra)-(i-1)])


#questao 5

# # Lê a sequência de caracteres do usuário
# sequencia = input("Digite a sequência de caracteres: ")

# # Remove espaços e pontuações da sequência
# sequencia = sequencia.replace(" ", "").replace(",", "").replace(".", "").lower()

# # Verifica se a sequência é um palíndromo
# if sequencia == sequencia[::-1]:
#     print("A sequência é um palíndromo.")
# else:
#     print("A sequência não é um palíndromo.")


#questao 6
# def complemento_dna(cadeia):
#     complemento = ''
#     for nucleotideo in cadeia:
#         if nucleotideo == 'A':
#             complemento += 'T'
#         elif nucleotideo == 'T':
#             complemento += 'A'
#         elif nucleotideo == 'C':
#             complemento += 'G'
#         elif nucleotideo == 'G':
#             complemento += 'C'
#     return complemento

# # Exemplo de uso da função
# cadeia_dna = 'AATCTGCAC'
# cadeia_complementar = complemento_dna(cadeia_dna)
# print(cadeia_complementar)


#questao 7
# from datetime import datetime

# # leitura da data de nascimento
# data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")

# # conversão da string para o objeto datetime
# data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

# # formatação da data com mês por extenso
# mes_extenso = data_nascimento.strftime("%B")

# # impressão do resultado
# print("Você nasceu em", data_nascimento.strftime("%d"), "de", mes_extenso, "de", data_nascimento.strftime("%Y"))


#questao 8

# string1 = input("Digite a primeira string: ")
# string2 = input("Digite a segunda string: ")

# posicao = string1.find(string2)

# if posicao == -1:
#     print(f"{string2} não foi encontrada em {string1}.")
# else:
#     print(f"{string2} encontrada na posição {posicao + 1} de {string1}.")


#questao 9

# str1 = input("Digite a primeira string: ")
# str2 = input("Digite a segunda string: ")
# str3 = ""

# for char in str1:
#     if char in str2 and char not in str3:
#         str3 += char

# print("A terceira string é:", str3)

#questao 10

# frase = input("Digite uma frase: ")
# espacos = 0
# vogais_a = 0
# vogais_e = 0
# vogais_i = 0
# vogais_o = 0
# vogais_u = 0

# for letra in frase:
#     if letra == " ":
#         espacos += 1
#     elif letra in "aeiouAEIOU":
#         if letra == "a" or letra == "A":
#             vogais_a += 1
#         elif letra == "e" or letra == "E":
#             vogais_e += 1
#         elif letra == "i" or letra == "I":
#             vogais_i += 1
#         elif letra == "o" or letra == "O":
#             vogais_o += 1
#         elif letra == "u" or letra == "U":
#             vogais_u += 1

# print("A frase digitada contém {} espaços em branco.".format(espacos))
# print("A letra 'a' aparece {} vezes na frase.".format(vogais_a))
# print("A letra 'e' aparece {} vezes na frase.".format(vogais_e))
# print("A letra 'i' aparece {} vezes na frase.".format(vogais_i))
# print("A letra 'o' aparece {} vezes na frase.".format(vogais_o))
# print("A letra 'u' aparece {} vezes na frase.".format(vogais_u))


#questao 11

# string = input("Digite uma string: ")

# # cria um dicionário para armazenar a quantidade de cada caractere
# caracteres = {}

# # percorre cada caractere da string
# for c in string:
#     # se o caractere já existe no dicionário, incrementa a quantidade
#     if c in caracteres:
#         caracteres[c] += 1
#     # senão, adiciona o caractere ao dicionário com quantidade 1
#     else:
#         caracteres[c] = 1

# # percorre o dicionário e imprime a quantidade de cada caractere
# for c in caracteres:
#     print(c + ": " + str(caracteres[c]) + "x")

#questao 12

# Definição das listas com os nomes dos números
# unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
# dezenas = ['dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
# dezenas2 = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']

# # Leitura do número
# numero = int(input('Digite um número entre 1 e 99: '))

# # Verificação do número digitado
# if numero < 1 or numero > 99:
#     print('Número inválido. Digite um número entre 1 e 99.')
# else:
#     # Caso o número seja menor que 10
#     if numero < 10:
#         print(unidades[numero])
#     # Caso o número seja maior ou igual a 10 e menor que 20
#     elif numero < 20:
#         print(dezenas[numero - 10])
#     # Caso o número seja maior ou igual a 20 e menor que 100
#     else:
#         unidade = numero % 10
#         dezena = (numero // 10) - 2
#         if unidade == 0:
#             print(dezenas2[dezena])
#         else:
#             print(dezenas2[dezena] + ' e ' + unidades[unidade])

#questao 13


# palavra = input("Digite uma palavra: ")
# resultado = ""

# for letra in palavra:
#     codigo_ascii = ord(letra) + 1
#     nova_letra = chr(codigo_ascii)
#     resultado += nova_letra

# print("Palavra encriptada: ", resultado)

#questao 14

# string = input("Digite uma string: ")
# nova_string = ""

# for c in string:
#     codigo_ascii = ord(c)
#     if 97 <= codigo_ascii <= 122:  # verifica se é letra minúscula
#         codigo_ascii -= 32  # converte para maiúscula
#     nova_string += chr(codigo_ascii)

# print("String em maiúsculas:", nova_string)

#questao 15

# # solicita a string ao usuário
# string = input("Digite uma string: ")

# # solicita as letras L1 e L2 ao usuário
# L1 = input("Digite a letra a ser substituída: ")
# L2 = input("Digite a letra para substituir: ")

# # converte a string para uma lista de caracteres
# lista_caracteres = list(string)

# # percorre a lista e substitui as letras L1 e L2
# for i in range(len(lista_caracteres)):
#     if lista_caracteres[i] == L1:
#         lista_caracteres[i] = L2
#     elif lista_caracteres[i] == L2:
#         lista_caracteres[i] = L1

# # converte a lista de volta para uma string e imprime
# nova_string = "".join(lista_caracteres)
# print("Nova string:", nova_string)


#questao 16

# # solicita a string ao usuário
# string = input("Digite uma string: ")

# # solicita as letras L1 e L2 ao usuário
# L1 = input("Digite a letra a ser substituída: ")
# L2 = input("Digite a letra para substituir: ")

# # converte a string para uma lista de caracteres
# lista_caracteres = list(string)

# # percorre a lista e substitui as letras L1 e L2
# for i in range(len(lista_caracteres)):
#     if lista_caracteres[i] == L1:
#         lista_caracteres[i] = L2
#     elif lista_caracteres[i] == L2:
#         lista_caracteres[i] = L1

# # converte a lista de volta para uma string e imprime
# nova_string = "".join(lista_caracteres)
# print("Nova string:", nova_string)

#questao 17

# pares = []
# impares = []

# for i in range(10):
#     num = int(input("Digite um número inteiro: "))
#     if num % 2 == 0:
#         pares.append(num)
#     else:
#         impares.append(num)

# print("Lista de pares:", pares)
# print("Lista de ímpares:", impares)

#questao 18

# idades = []
# alturas = []

# for i in range(4):
#     idade = int(input("Digite a idade do aluno {}: ".format(i+1)))
#     altura = float(input("Digite a altura do aluno {}: ".format(i+1)))
#     idades.append(idade)
#     alturas.append(altura)

# media_alturas = sum(alturas) / len(alturas)
# cont_alunos = 0

# for i in range(4):
#     if idades[i] > 13 and alturas[i] < media_alturas:
#         cont_alunos += 1

# print("Número de alunos com mais de 13 anos e altura inferior à média: {}".format(cont_alunos))


#questao 19

# quantidade_alunos = int(input("Digite a quantidade de alunos: "))

# idades = []
# alturas = []

# for i in range(quantidade_alunos):
#     print(f"Aluno {i+1}:")
#     idade = int(input("Digite a idade: "))
#     altura = float(input("Digite a altura em metros: "))
#     idades.append(idade)
#     alturas.append(altura)

# media_alturas = sum(alturas) / quantidade_alunos

# alunos_baixa_altura = 0
# for i in range(quantidade_alunos):
#     if idades[i] > 13 and alturas[i] < media_alturas:
#         alunos_baixa_altura += 1

# print(f"{alunos_baixa_altura} alunos com mais de 13 anos possuem uma altura inferior à média de altura dos alunos.")


#questao 20

# alunos_idades = []
# alunos_alturas = []

# while True:
#     idade = int(input("Digite a idade do aluno (digite um valor negativo para encerrar a leitura): "))
#     if idade < 0:
#         break
#     altura = float(input("Digite a altura do aluno: "))
#     alunos_idades.append(idade)
#     alunos_alturas.append(altura)

# media_alturas = sum(alunos_alturas) / len(alunos_alturas)
# alunos_abaixo_media = 0

# for i in range(len(alunos_idades)):
#     if alunos_idades[i] > 13 and alunos_alturas[i] < media_alturas:
#         alunos_abaixo_media += 1

# print(f"Existem {alunos_abaixo_media} alunos com mais de 13 anos e altura abaixo da média de todos os alunos.")


#questao 21

# meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
#          'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

# data = input("Digite a data de nascimento (dd/mm/aaaa): ")
# dia, mes, ano = data.split('/')

# mes_extenso = meses[int(mes) - 1]

# print(f"Você nasceu em {dia} de {mes_extenso} de {ano}")

#questao 22

# import datetime

# # Ler as temperaturas médias de cada mês
# temperaturas = []
# for mes in range(1, 13):
#     temperatura = float(input(f"Temperatura média do mês {mes}: "))
#     temperaturas.append(temperatura)

# # Calcular a média anual das temperaturas
# media_anual = sum(temperaturas) / len(temperaturas)

# # Percorrer a lista de temperaturas e imprimir as que estão acima da média anual
# for mes, temperatura in enumerate(temperaturas):
#     if temperatura > media_anual:
#         nome_mes = datetime.date(2000, mes+1, 1).strftime('%B')
#         print(f"{nome_mes}: {temperatura}°C")


#questao 23

# # criando uma lista vazia para armazenar os resultados
# resultados = []

# loop infinito para receber os dados dos atletas
# while True:
#     nome = input("Digite o nome do atleta: ")
    
#     # encerrando o programa caso o nome não seja informado
#     if nome == "":
#         break
    
#     # criando uma lista para armazenar as distâncias dos saltos
#     saltos = []
#     for i in range(1, 6):
#         salto = float(input(f"Digite a distância do {i}º salto: "))
#         saltos.append(salto)
    
#     # calculando a média dos saltos
#     media = sum(saltos) / len(saltos)
    
#     # adicionando o resultado na lista de resultados
#     resultados.append([nome, saltos, media])

# # exibindo os resultados
# print("Resultado final:")
# for resultado in resultados:
#     nome = resultado[0]
#     saltos = resultado[1]
#     media = resultado[2]
    
#     print(f"Atleta: {nome}")
#     print(f"Saltos: {saltos}")
#     print(f"Média dos saltos: {media:.2f}")
#     print()

ref_arquivo = open("notas_estudantes.txt","r")
linhas = ref_arquivo.readlines()
ref_arquivo.close()


for linha in linhas:
    dados_aluno = linha.strip().split(" ")
    nome_aluno = dados_aluno[0]
    notas_aluno = int(dados_aluno[1:])
    media = 0
    divisor =0
    mediaFinal = 0
    for nota in notas_aluno:   
        divisor+=1
        media+=nota
        mediaFinal = media/divisor
print(nome_aluno,"media:", mediaFinal)       
       



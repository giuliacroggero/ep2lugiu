def define_posicoes(linha,coluna,orientacao,tamanho):
    lista = []
    i = 0
    if orientacao == 'vertical':
        while len(lista)<tamanho:
            lista.append([linha+i,coluna])
            i+=1
        
    elif orientacao == 'horizontal':
        while len(lista)<tamanho:
            lista.append([linha,coluna+i])
            i+=1
    return lista

linha = 2
coluna = 4
orientacao = 'horizontal'
tamanho = 3
print(define_posicoes(linha,coluna,orientacao,tamanho))
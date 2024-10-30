# Função de Merge Sort
def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        # Chamada recursiva para cada metade
        merge_sort(esquerda)
        merge_sort(direita)

        # Variáveis de índice para cada metade
        i = j = k = 0

        # Merge das duas metades
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        # Verificar se restaram elementos na metade esquerda
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        # Verificar se restaram elementos na metade direita
        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

# Leitura e Ordenação do Arquivo
with open('extra.txt', 'r') as arquivo:
    linhas = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena em uma lista

# Remover caracteres de nova linha e ordenar com merge_sort
linhas = [linha.strip() for linha in linhas]  # Remove '\n' de cada linha
merge_sort(linhas)  # Ordena a lista de linhas usando merge sort

# Exibir o Conteúdo Ordenado
for linha in linhas:
    print(linha)

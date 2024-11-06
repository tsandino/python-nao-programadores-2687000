# Crie uma lista apenas com elementos numéricos
lista = [0, 1, 2, 3, 4]
print(lista)
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
lista_mista = [0, 1, "Tiago", [], [2, 3, 4], True]
print(lista_mista)
# Imprima na tela apenas os 5 primeiros elementos da lista
print(lista_mista[0:5])
# Crie um slice na lista para que imprima na tela os elementos de índice par
print(lista_mista[::2])
# Remova da lista o último item
lista_mista.remove(True)
print(lista_mista)
# Insira na lista um novo item
lista_mista.extend(["Python", "SQL", "Javascript"])
print(lista_mista)
# Remova da lista um item específico
lista_mista.remove("Tiago")
print(lista_mista)
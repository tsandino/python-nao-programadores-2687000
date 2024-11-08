# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
cursos = ['SQL: Primeiros Passos', 'Python para não programadores', 'Introdução à Inteligência Artificial',
          'Ciência de Dados: Formação Básica', 'Descubra a Linguagem R']

# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
curso_SQL = 'SQL: Primeiros Passos'
curso_Pyhon = 'Python para não programadores'
curso_R = 'Descubra a Linguagem R'

# 3. Crie um dicionário vazio para armazenar a nota do curso
avaliacoes = {}
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
if curso_Pyhon in cursos:
  print(f"O curso {curso_Pyhon} está no catálogo. Por favor avalie o curso.")
  avaliacoes[curso_Pyhon] = int(input('Qual a nota que você dá para o curso (0 a 5)? '))

if curso_SQL in cursos:
  print(f"O curso {curso_SQL} está no catálogo. Por favor avalie o curso.")
  avaliacoes[curso_SQL] = int(input('Qual a nota que você dá para o curso (0 a 5) ?'))

if curso_R in cursos:
  print(f"O curso {curso_R} está no catálogo. Por favor avalie o curso.")
  avaliacoes[curso_Pyhon] = int(input('Qual a nota que você dá para o curso (0 a 5) ?'))

else:
  print('Infelizmente, o curso não compõe nosso catálogo.')

# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota
print(avaliacoes)

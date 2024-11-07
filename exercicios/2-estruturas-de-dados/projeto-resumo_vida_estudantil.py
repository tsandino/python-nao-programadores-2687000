# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
estudante = {}
estudante['nome'] = input('Qual o seu nome? ')
estudante['ano_linkedin'] = int(input ('Em que ano conheceu o LinkedIn? '))
estudante['ano_atual'] = int(input('Em que ano está respondendo essa pesquisa? '))
cursos_linkedin = input('Liste em ordem cronológica e separados por vírgula, os cursos que você já realizou no LinkedIn Learning: ')
estudante['cursos_linkedin'] = cursos_linkedin.split(', ')

# 2. Armazene esses dados em um dicionário

# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
total_anos = estudante['ano_atual'] - estudante['ano_linkedin']
total_cursos = len(estudante['cursos_linkedin'])
print(f"Olá, {estudante['nome']}! Desde {estudante['ano_linkedin']} você conhece o LinkedIn. Nesses {total_anos} anos, você realizou {total_cursos} cursos, sendo o primeiro '{estudante['cursos_linkedin'][0]}' e o último curso '{estudante['cursos_linkedin'][-1]}'.")

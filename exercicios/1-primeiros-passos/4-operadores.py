ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
idade_formatura = ano_formatura - ano_nascimento
print(f"Gerlaine tinha {idade_formatura} anos quando se formou")
# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
print(idade_formatura > 18)
print(idade_formatura <= 18)
print(idade_formatura == 18)
# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
nome = "Gerlaine"
print(idade_formatura > 18 and nome == "Gerlaine")
print(idade_formatura == 21 or nome == "Tiago")
print(not(idade_formatura > 18))
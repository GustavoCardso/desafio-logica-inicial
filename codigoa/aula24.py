#nome = 'gustavo'
#print(nome[3])
#print('u' in nome)
#print('g' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Escreva o que deseja encontar: ')
if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
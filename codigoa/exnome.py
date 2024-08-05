nome = input('digite seu nome: ')
if nome:
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome tem espaço')
    else:
        print('seu nome não tem espaço')
quantidade_de_letra = len(nome)
print(f'seu nome tem {quantidade_de_letra} letras')
print(f'a primeira letra do seu nome é {nome[:1]}')
print(f'A ultima letra do seu nome é {nome[-1]}')
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
if nome and idade:
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')
    if " " in nome:
        print(f'seu nome contem espaços')
    else:
        print('Seu nome não contem espaços')

    print(f'seu nome tem {len(nome)} letras')
    print(f'A ultima letra do seu nome é:{nome[-1]}')

else:
    print('voce nao digitou nada')
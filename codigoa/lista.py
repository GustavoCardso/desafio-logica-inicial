while True:
    numero_1 = input(('digite um numero: '))
    numero_2 = input(('digite outro numero: '))
    operador = input(('digite um operador (+,-./,*)'))
    numeros_validos = None
    numero_1_float = 0
    nume_2_float = 0

    try:
        nume_1_float =  float(numero_1)
        nume_2_float = float(numero_2)
        numeros_validos = True
    except: 
        numeros_validos is None
    
    if numeros_validos is None:
        print('Um ou ambos numero digitado são invalidos')
        continue
    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Operador invalido')
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    if operador == '+':
        print(f'{nume_1_float} + {nume_2_float} =', nume_1_float + nume_2_float)
    elif operador == '-':
        print(f'{nume_1_float} - {nume_2_float} =', nume_1_float - nume_2_float)
    elif operador == '/':
        print(f'{nume_1_float} / {nume_2_float} =', nume_1_float / nume_2_float)
    elif operador == '*':
        print(f'{nume_1_float} * {nume_2_float} =', nume_1_float * nume_2_float)
    else:
        ('nunca deveria chegar aqui')
    
    sair = input('Voce quer [s]air?: ').lower().startswith('s') 


    

    if sair == True:
        break
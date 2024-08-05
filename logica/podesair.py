tempo = input('O tempo é de sol ou chuva? ')
item = input('voce esta com um guarda chuva? ')

while tempo != 'chuva':
    print('pode sair')
    break
while  tempo == 'chuva':
    print('espere a chuva passar')
    continue
if item != 'sim':
    print('pegue o guarda chuva')


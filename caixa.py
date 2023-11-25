print('Banco de ESTUDOS')
sacar = int(input('Quanto você vai sacar?'))
total = sacar
ced = 50
totalced =0
print('-='*30)
while True:
    if total >= ced:
        total -= ced
        totalced +=1
    else:
        if totalced >0:
            print(f'Total de {totalced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        if ced == 20:
            ced = 10
        if ced == 10:
            ced =1
        if total ==0:
            break
print('-='*30)
print('Volte sempre ao BANCO DE ESTUDOS! Tenha um bom dia')

#nome = 'Rodrigo Lara'
nome = input('Qual é seu nome? ')
#altura = 1.65
altura = input('Qual é sua altura? ')
float_altura = float(altura.replace(',','.'))
#peso = 86
peso = input('Qual é seu peso? ')
float_peso = float(peso.replace(',','.'))

imc = float_peso / (float_altura ** 2) 

linha_1 = f'{nome} tem {altura} de altura,' 
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'


print(linha_1)
print(linha_2)
print(linha_3)

if imc < 18.5:
    print('Abaixo do Peso')
elif imc > 18.5 and imc < 24.9:
    print('Peso Normal')
elif imc > 25 and imc < 29.9:
    print('Sobrepeso')
elif imc > 30 and imc < 34.9:
    print('Obesidade grau I')
elif imc > 35 and imc < 39.9:
    print('Obesidade grau II')
else:
    print('Obesidade grau III')
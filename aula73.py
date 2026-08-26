
texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')

"""
For + Range
range -> range(start, stop, step)
"""
numeros = range(0, 100, 8)

print('')
for numero in numeros:
    print(numero)
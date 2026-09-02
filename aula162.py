# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
from dados.produtos import produtos as prods

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
import copy

novos_produtos = [ 
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(prods)
]

#for produto in prods:
#    produto['preco'] = round(produto['preco'] * 1.1, 2)

print(*novos_produtos, sep='\n')
print('')
print(*prods, sep='\n')

produtos_ordenados_por_nome = copy.deepcopy(prods)
produtos_ordenados_por_nome = sorted(
    produtos_ordenados_por_nome,
    key=lambda p:p['nome'],
    reverse=True
)

print('')
print(*produtos_ordenados_por_nome, sep='\n')

produtos_ordenados_por_preco = copy.deepcopy(prods)
produtos_ordenados_por_preco = sorted(
    produtos_ordenados_por_preco,
    key=lambda p:p['preco']
)

print('')
print(*produtos_ordenados_por_preco, sep='\n')


def calcular_total(compras):
  total = 0
  for produto in compras:
      total += produto['quantidade'] * produto['preco_unitario']
  return total


lista_de_compras = [
  {'nome': 'Banana', 'quantidade': 3, 'preco_unitario': 1.50},
  {'nome': 'Pão', 'quantidade': 2, 'preco_unitario': 2.00},
  {'nome': 'Tapioca', 'quantidade': 1, 'preco_unitario': 5.00},
]

valor_total = calcular_total(lista_de_compras)
print(f'Valor total da compra: R${valor_total:.2f}')

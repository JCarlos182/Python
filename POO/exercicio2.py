"""
## Classe Produto e método desconto

Desenvolva uma classe em Python para atender as seguintes especificidades de um Produto:

1. Cada produto deve ter um preço e um nome.
2. A classe deve ter um método construtor e o método dundle str.
3. A classe deve ter um método para desconto. O método deve receber o desconto em percentual
 e realizar o cálculo de quanto ficaria o preço final com o desconto.
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Produto {self.name} - R$ {self.price} reais"

    def discount(self, perc_discount):
        valorDiscount = (self.price/100) * perc_discount
        finalPrice = self.price - valorDiscount
        return int(finalPrice)

xbox = Product("Xbox Series X", 4500)
iphone = Product("Iphone 15 Pro", 7500)
print(xbox)
print(iphone)
print(xbox.discount(10))
print(iphone.discount(15))

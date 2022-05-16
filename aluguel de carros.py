dias = int(input('Quantos dias o carro foi usado?'))
km = float(input('Quantos KM rodados?'))
pago = dias * 60 + (km * 0.15)
print('o total a pagar é de R${:.2f}'.format(pago))

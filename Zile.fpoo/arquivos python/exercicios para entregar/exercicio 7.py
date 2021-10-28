nome = str(input('Informe o seu nome: '))
idade = int(input('Informe a sua idade: '))
tempo = int(input('Você é cliente da loja a quanto tempo?: '))
valor = float(input('Informe o valor da compra: '))
parcela = int(input('Vai parcelar em quantas vezes?: '))
desconto = 0
if parcela <= 1:
 desconto = (valor * 10) / 100
if parcela > 1 and parcela <= 6:
 desconto = (valor * 5) / 100
if valor > 5000 or tempo > 6 or idade >= 60:
 desconto = (valor * 5) / 100
if parcela <= 1 and valor > 5000 or tempo > 6 or idade >= 60:
 desconto = (valor * 15) / 100
print('----------')
print('Valor da compra: R${}'.format(valor))
print('Valor do desconto: R${}'.format(desconto))
print('Preço final: R${}'.format(valor - desconto))

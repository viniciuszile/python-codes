hora_entrada = float (input("informe as horas de entrada :"))
min_entrada = float (input("informe os minutos de entrada :"))
hora_saida  = float (input("informe as horas de saida :"))
min_saida = float (input("informe os minutos de saida :"))

#caso tempo dentro do estacionamento seja menos que 24 horas
if hora_entrada < hora_saida :
    horas = hora_saida - hora_entrada

#caso tempo dentro do estacionamento seja mais que 24 horas
elif hora_entrada > hora_saida :
    horas = (24-hora_entrada) + hora_saida


if min_entrada <= min_saida:
    min_hora = int ((min_saida-min_entrada)/60)

elif min_entrada >= min_saida:
    min_hora = int (((60 - min_entrada)+min_saida)/60)
total = horas + min_hora

if total <3:
    valor = 20
elif total >= 3 and total < 5:
    valor = 32
elif total >= 5:
    valor = (total*8)

print ("o valor total a pagar é {:.2f}".format (valor))
print ("quantidade de horas que voce ficou no estacionamento {:.0f}".format (horas))           



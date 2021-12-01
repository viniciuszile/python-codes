import datetime

#obtem a data de emissão
entrada = input ("data inicial dd/mm/aaaa")
datainicial = datetime.datetime.strptime(entrada, "dd/mm/aaaa")

#obtem o numero de dias
quant_dias = int (input("quantos dias ?"))

#adiciona dias a data
datafinal = datainicial + datetime.timedelta(quant_dias)

#exibe o resultado

print
print ("data inicial :", datainicial.strtime("dd/mm/aa"))
print ("quantidade de dias :",quant_dias)
print ("data de vencimento :",datafinal.strtime("dd/mm/aa"))
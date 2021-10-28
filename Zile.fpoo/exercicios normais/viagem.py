resultado = 0

#mes ferias
print ("1 - para sim ")
print ("2 - para não")
ferias_maria = int (input("maria sai de feiras em dezembro ? :"))
ferias_marcos = int (input("marcos sai de ferias em dezembro :"))

if (ferias_maria == 1) and (ferias_marcos == 1):
    resultado = resultado +1

#13 salario 
print ("-"*50)
print ("1 - para sim ")
print ("2 - para não")
mes_maria = int (input("maria recebe o 13 salario antes do dia 12/12 ?"))   
mes_marcos = int (input("marcos recebe o 13 salario antes do dia 12/12 ?")) 

if (mes_maria == 1) or (mes_marcos == 1):
    resultado = resultado + 1

#nota carla
print ("-"*50)
print ("1 - para sim ")
print ("2 - para não")
nota = int (input("o nota de carla na escola foi maior que 7(70)? "))
if (nota == 1):
    resultado = resultado + 1

#total gastos    
print ("-"*50)
print ("1 - para maior ")
print ("2 - para menor")
gastos = int (input("o valor total da reserva do hotel e das passagens de avião é igual ou inferior a R$ 10.000,00 ?"))
if (gastos == 2):
    resultado = resultado + 1

#resultado final 
if (resultado == 4):
    print ("-"*50)
    print ("parabens maria e marcos cumpriram os 4 requisitos ")
    
else:
        print ("-"*50)
        print ("maria e marcos não cumpriram os 4 requisitos")   



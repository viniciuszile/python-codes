print ("-"*90)
print ("para continuar informe um numero positivio")
print ("para sair informe um numero negativo")
x = int (input(":"))
print ("-"*90)
while (x > 0):
    exesso = 50
    
    peso = float (input("escreva quantos KG de peixes voce trouxe :"))
    
    if (peso > 50):
        exesso = (peso - exesso)
        multa = exesso * 40
        print ("o total de KG em exesso é :",exesso)
        print ("A multa que devera ser paga é:",multa)
        print ("-"*90)
        print ("para continuar informe um numero positivio")
        print ("para sair informe um numero negativo")
        x = int (input("-"))
        print ("-"*90)

    elif (peso <= 50):
        print ("o total de KG em exesso é :",exesso)
        print ("Nao havera multa ")
        print ("-"*90)
        print ("para continuar informe um numero positivio")
        print ("para sair informe um numero negativo")
        x = int (input(":"))
        print ("-"*90)    

        
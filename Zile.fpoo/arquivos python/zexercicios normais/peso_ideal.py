
print ("---------------------------------------")
print ("informe um numero negativo para sair")
print ("informe um numero poaitivo para continuar")
x = int (input("deseja calcular seu peso ideal?|"))
print ("---------------------------------------")
while (x > 0 ):

    print ("-"*90)
    print (" 1- masculino ")
    print (" 2- feminino ")
    sexo = int (input("escolha qual seu sexo :"))
    print ("-"*90)
    altura = float (input("informe a sua altura:"))
    print ("-"*90)
    peso = float (input("informe o seu peso :"))
    print ("-"*90)

    if (sexo == 1):
        peso_i = (72.2 * altura) -58

    elif (sexo == 2):
        peso_i = (62.1 * altura) -44.7

    print ("seu peso :",peso)
    print ("-"*90)
    print ("seu peso ideal:",peso_i)
    print ("-"*90)

    if (peso_i < peso):
        print ("voce esta abaixo do seu peso ideal")

    elif (peso_i == peso):
        print ("voce esta no seu peso ideal")

    elif (peso_i > peso):
        print ("voce esta acima do seu peso ideal")     

    print ("---------------------------------------")
    print ("informe um numero negativo para sair")
    print ("informe um numero poaitivo para continuar ")
    x = int (input("deseja calcular seu peso ideal?"))
    print ("---------------------------------------")
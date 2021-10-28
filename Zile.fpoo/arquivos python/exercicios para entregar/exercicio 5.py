print ("1- homem")
print ("2- mulher")
print ("-"*100)

sexo = float (input("escolha seu sexo"))
altura = float (input("informe sua altura:"))

if (sexo == 1):
    peso = (altura - 100)*0.90
    print ("seu peso ideal é :",peso)

if (sexo == 2):
    peso = (altura - 100)*0.85
    print ("seu peso ideal é ",peso)
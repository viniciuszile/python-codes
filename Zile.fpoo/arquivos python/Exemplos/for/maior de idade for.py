hoje = 2021
cont = 0

for x in range (1,8):
    nacimento = int (input("informe o ano em que voçê nasceu :"))
    idade = hoje -  nacimento

    if (idade >= 18):
        cont = cont + 1

print ("-"*99)
print ("o numero de pessoas que não são maiores de idade é",cont)        
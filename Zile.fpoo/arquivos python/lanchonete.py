from time import sleep
#contadores produto 
c_coxinha = 0
c_pao = 0
c_misto = 0
c_empada = 0 
c_croa = 0
c_sonho = 0
c_rosquinha = 0
c_carolinas = 0
c_bolo = 0
c_pudim = 0
c_cafe = 0
c_capu = 0
c_leite = 0
c_suco = 0
c_refri = 0
#contadores pruduto 
total = 0

#saida 
print ("-"*99)
print ("seja bem vindo a nossa lanchonte!")
print ("-"*99)
while True:
    x = int  (input("deseja pedir algum lanche ? S(1) N(-1)"))
    print ("-"*99)
    if x !=1 and x!= -1:
        print ("ERRO! escolha uma opção valida ")
    else:
        break    
print ("-"*99)

while (x >= 0):
        while True :
            print ("veja nossas opçoes de lanches : ")
            print ("="*77)
            print ("|0- nenhum              |                         |                         |")
            print ("|1- coxinha (3R$)       |6- sonho (R$3)           |11- cafe preto (R$2)     |")
            print ("|2- pão de queijo (2R$) |7- rosquinha (R$4)       |12- cappuccino (R$6)     |")
            print ("|3- misto quente (7R$)  |8- carolinas 3xuni (R$1) |13- cafe com leite (R$3) |")
            print ("|4- empada (4R$)        |9- pedaço de bolo (R$7)  |14- suco natural (R$4)   |")
            print ("|5- croissant (5R$)     |10- pudim de leite (R$6) |15- refri lata (R$5)     |")
            print ("="*77)
            lanche = int  (input("informe qual desses lanche voçê deseja :"))
            if lanche < 0 or lanche > 15:
                print ("Por favor escolha um numero da tabela acima ")
                print ("="*99)
                sleep(1)
            else:
                break
            
        
        
        print ("="*99)
        if (lanche == 1):
            total = total + 3
            c_coxinha = c_coxinha + 1
        
        elif (lanche == 2):
            total = total + 2
            c_pao = c_pao + 1
        
        elif (lanche == 3):
            total = total + 7
            c_misto = c_misto + 1
        
        elif (lanche == 4):
            total = total + 4
            c_empada = c_empada + 1
        
        elif (lanche == 5):
            total = total + 5
            c_croa = c_croa + 1

        elif (lanche == 6 ):
            total = total + 3
            c_sonho = c_sonho + 1

        elif (lanche == 7):
            total = total + 4
            c_rosquinha = c_rosquinha +1

        elif (lanche == 8):
            total = total + 1
            c_carolinas = c_carolinas + 1

        elif (lanche == 9):
            total = total + 7
            c_bolo = c_bolo + 1

        elif (lanche == 10):
            total = total + 6
            c_pudim = c_pudim + 1

        elif (lanche == 11):
            total = total + 2
            c_cafe = c_cafe + 1

        elif (lanche == 12):
            total = total + 6
            c_capu = c_capu + 1

        elif (lanche == 13):
            total = total + 3
            c_leite = c_leite + 1

        elif (lanche == 14):
            total = total + 4
            c_suco = c_suco + 1

        elif (lanche == 15):
            total = total + 5
            c_refri = c_refri + 1                   
        #saida
        while True:
            x = int  (input("deseja pedir mais algum lanche ? S(1) N(-1)"))
            print ("-"*99)
            if x !=1 and x!= -1:
                print ("ERRO! escolha uma opção valida")
            else:
                break    

print ("================================")
print ("|       resumo do pedido       |")
print ("================================")
if (c_coxinha > 0):
    print ("|       coxinhas x",c_coxinha,'          |') #13

if (c_pao > 0):
        print ("|       pão de queijo x",c_pao,'     |') #18
    
if (c_misto > 0):
        print ("|       misto quente x",c_misto,'      |') #17

if (c_empada > 0):
        print ("|       empada x",c_empada,'            |') #11
if (c_croa > 0):
        print ("|       croissant x",c_croa,'         |') #14      
    
if (c_sonho > 0):
        print ("|       sonho x",c_sonho,'             |') #10  

if (c_rosquinha > 0):
        print ("|       rosquinha x",c_sonho,'         |')  #14
    
if (c_carolinas > 0):
        print ("|       carolinas (3x) x",c_carolinas,'    |')   #19
    
if (c_bolo > 0):
        print ("|       pedaço de bolo x",c_bolo,'    |')  #19
    
if (c_pudim > 0):
        print ("|       pudim de leite x",c_pudim,'    |')  #19
    
if (c_cafe > 0):
        print ("|       cafe preto x",c_cafe,'        |')  #15
    
if (c_capu > 0):
        print ("|       cappucino x",c_capu,'         |')  #14
    
if (c_leite > 0):
        print ("|       cafe com leite x",c_leite,'    |')  #19
    
if (c_suco > 0):
        print ("|       suco natural x",c_suco,'      |') #17 
    
if (c_refri > 0):
        print ("|       refri lata x",c_refri,'        |')  #15

print ("================================")

print ("|     total do valor ",total,'       |') #17
 
print ("================================")









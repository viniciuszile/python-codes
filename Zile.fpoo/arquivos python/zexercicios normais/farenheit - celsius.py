    #faça um programa que peça a temperatura em farenheit, transforme e mostre a temperatura em celsius..

print ("escolha uma das opçoes abaixo")
print ("1- celsius---farenheit")
print ("2- farenheit---celsius")
print ("3- celsius---kelvin")
print ("4- kelvin---celsius")

t = float(input ("escolha uma das opçoes acima"))

if (t == 1):

 c = float (input("informe sua temperatura em celsius :"))
 f = c*1.8 +32
 print ("sua temperatura convertida de celsius para farenheit é :",f)
  
if (t == 2):
 f = float (input("informe sua temperatura em farenheit :"))
 c = (5*(f -32)/9)
 print ("sua temperatura convertida de farenheit para celsius é :", c)

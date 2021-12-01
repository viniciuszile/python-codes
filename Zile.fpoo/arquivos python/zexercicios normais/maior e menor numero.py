#faça um programa que leia 3 numeros e mostre o menor deles
print ("---------------------------------------")
n1 = float (input("informe o primeiro valor :"))

print ("---------------------------------------")
n2 = float (input("informe o segundo valor :"))

print ("---------------------------------------")
n3 = float (input("informe o terceiro valor :"))
print ("---------------------------------------")

if (n1 > n2 ) & (n1 > n3):
 print ("o maior numero é",n1)
elif (n2 > n1 ) & (n2 > n3):
 print ("o maior numero é",n2)
elif (n3 > n1 ) & (n3 > n2):
 print ("o maior numero é",n3)

if (n1 < n2 ) & (n1 < n3):
 print ("o menor numero é",n1)
elif (n2 < n1 ) & (n2 < n3):
 print ("o menor numero é",n2)
elif (n3 < n1 ) & (n3 < n2):
 print ("o menor numero é",n3)


elif (n1 == n2) & (n1 == n3):
 print (" sinto muito os valores sao iguais")



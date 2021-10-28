maior = 0
menor = 0
acum = 0
cont = 0
cont2 = 0
mais_velho = str
 
for i in range (1,5):
    cont = cont + 1
    print('')
    print ('-------------------------')
    nome = str (input('Digite o seu nome: '))
    print ('-------------------------')
    idade = int (input('Digite a sua idade: '))
    print ('')
    print ('-------------------------')
    print ('| M | F ')
    print ('--------------------------')
    sexo = str (input('Digite o seu sexo de acordo com a tabela acima: '))
    
    if (sexo == 'M' ) or (sexo == 'm') and (idade > maior):
         maior = idade
         mais_velho = nome
    
    if (sexo == 'F' ) or (sexo == 'f') and (idade < 20):
        cont2 = cont2 + 1
    
    
    acum = acum + idade
 
    media = (acum / cont)
 
print ('')
print ('A media de idade do grupo é:',media)
print ('O nome do homem mais velho é:',mais_velho)
print ('A quantidade de mulheres que tem menos de 20 anos é:',cont2)
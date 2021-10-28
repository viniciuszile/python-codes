salario = float (input("informe o seu salario :"))

if (salario <= 980):
    nsalario = salario*1.20
    print ("atual salario",salario)
    print ("novo salario",nsalario)

if (salario >= 981) and (salario <= 1700):
    nsalario = salario*1.15
    print ("atual salario",salario)
    print ("novo salario",nsalario)

if (salario >= 1701) and (salario <= 2500):
    nsalario = salario*1.10
    print ("atual salario",salario)
    print ("novo salario",nsalario)

if (salario > 2500):
    nsalario = salario*1.05
    print ("atual salario",salario)
    print ("novo salario",nsalario)    

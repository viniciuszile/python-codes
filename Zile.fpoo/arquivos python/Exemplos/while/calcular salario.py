salario_d = 0
salario_b = 0
salario_f = 0

print ("deseja continuar ? ")
print ("s/sim")
print ("n/não")

x = str (input("-"))

while (x == 's'):

    print ("-"*99)
    dias = int(input("informe quantos dias voçe trabalha pro mes :"))
    horas = int(input("informe quantas horas voçe trabalha por dia :"))
    d_h = float (input("informe quanto voçe recebe por hora trabalahada :"))
    print ("-"*99)

    salario_d = horas*d_h
    salario_b = salario_d*dias

    inss = salario_b*0.08
    imposto = salario_b*0.11
    sindicato = salario_b*0.05
    salario_f = (salario_b-inss-imposto-sindicato)

    print ("-"*99)
    print ("salario bruto sem descontos :",salario_b)

    print ("-"*99)
    print ("total descontado inss :",inss)

    print ("-"*99)
    print ("total descontado imposto de renda :",imposto)

    print ("-"*99)
    print ("total descontado sindicato :",sindicato)

    print ("-"*99)
    print ("total salario com todos os descontos :",salario_f)
    print ("-"*99)

    print ("-"*99)
    print ("deseja continuar ? ")
    print ("s/sim")
    print ("n/não")
    x = str (input("-"))

n1 = float (input("informe a sua primeira nota(de 0 a 100) :"))
n2 = float (input("informe a sua segunda nota (de 0 a 100):"))
frequencia = float (input("informe a sua frequencia nas aulas :"))
media = (n1+n2)/2

if (media >= 70 ) and (frequencia >= 75):
    print ("aluno aprovado")

if (media < 50) and (frequencia < 75):
    print ("aluno reprovado")

if (media <= 70) and (media >= 50) and (frequencia >= 50) and (frequencia <= 75):
    print ("recuperaçao")

   




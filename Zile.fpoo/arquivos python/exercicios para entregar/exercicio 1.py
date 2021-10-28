#o indice de massa corporal é um indicador adotado pela oms, é usado para o diagnostico do baixo peso, sobrepeso e da obsedade. 
#o IMC pode ser facilmente calculado a partir de dois dados peso e altura

peso = float (input("informe o seu peso(em kg) :"))
altura = float (input("informe a sua altura(em metros) :"))
imc = peso/altura**2

if (imc < 16):
    print ("baixo peso muito grave ") 


if (imc >=  16) and (imc <= 16.99):
    print ("baixo peso grave")


if (imc >= 17) and (imc <=  18.49):
    print ("baixo peso")

if (imc >= 18.50) and (imc <= 24.99):
    print ("peso normal")

if (imc >= 25) and (imc <= 29.99):
    print ("sobre peso")

if (imc >= 30) and (imc <= 34.99):
    print ("obesidade grau 1")

if (imc >= 35) and (imc <= 39.99):
    print ("obesidade grau 2")

if (imc >= 40 ):
    print ("obesidade grau 3(obesidade morbida)")     


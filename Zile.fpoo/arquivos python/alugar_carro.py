#data 
_ano = 2021
_mes = 10
_dia = 31


print ("-"*70)
print ("informe a sua data de nacimento")
print ("")
ano = int (input("informe o ano :"))
mes = int (input("informe o mes :"))
dia = int (input("informe o dia :"))

data_n = dia,mes,ano
x = _ano - ano

print ("-"*70)
nome = str (input("informe o seu nome :"))

print ("-"*70)
cnh = int (input("informe a sua CNH :"))

print ("-"*70)
km = float (input("quantos km foi rodado o veiculo ?"))

print ("-"*70)
dias = int (input("por quantos dias o veiculo foi usado ?"))

print ("-"*70)
print ("1 - grande")
print ("2 - medio")
print ("3 - pequeno")
porte = int (input("informe o porte do carro que voce deseja (1,2,3):"))

if (porte == 3 ):
    diaria = 180
elif (porte == 2):
    diaria = 220
elif (porteb == 1):
    diaria = 270         
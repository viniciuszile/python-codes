def calc1():
        return horas - 12
        
def calc2():
        return horas + 12
    
horas = 0
minutos = 0

saida = str (input("deseja usar nosso programa ? sim/nao"))

while saida == "sim" or saida == "SIM":
    print ("=-"*10)
    print ("informe o horario que voce deseja converter:")
    horas = int (input("informe as horas"))
    minutos = int (input("informe os minutos"))
    
    if (horas > 23) or (horas < 0):
        print ("error")
        break
    if (minutos < 0) or (minutos > 60):
        print ("error")
        break
    if  horas < 12:
        print("",calc2(),":",minutos,"PM")
    elif horas >= 12:
        print ("",calc1(),":",minutos,"AM")

    saida = str (input("deseja usar nosso programa ? sim/nao"))

print ("obrigado por usar o programa")

    

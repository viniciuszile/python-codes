medidas = float(input("insira o tamanho da area em metros quadrados :"))
litro_tinta = medidas/3
if litro_tinta <= 18:
    valor = 560
    qnt_lata = 1
elif litro_tinta>18:
    qnt_lata = (litro_tinta/18)+1
    valor = (int(qnt_lata))*560
print ("a quantide de latas sera de", int(qnt_lata),"e custara", valor) 
           
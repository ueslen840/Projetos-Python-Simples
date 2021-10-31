import os
os.system("cls") #limpar terminal
valorrestante = valor = int (input("quanto deseja sacar?\n")) # aqui o usurio escolhe quanto quer sacar e automaticamente adiciona-se o valor a variavel valorrestante para fins de contage sem perder o valor inicial
#começar contagem de notas em zero
fim=nota200=nota100=nota50=nota20=nota10=nota5=nota2=0
os.system("cls") #limpar terminal
print("contando, por favor, aguarde...")
#contador de notas
while fim<1: # aqui o software vai fazer a contagem ate acabar
    while valorrestante>=200: # aqui o software vai contar quantas notas de 200 reais serao sacadas, até nao ser possivel entregar notas de 200
        nota200=nota200+1
        valorrestante=valorrestante-200

    while valorrestante>=100:
        nota100=nota100+1
        valorrestante=valorrestante-100

    while valorrestante>=50:
        nota50=nota50+1
        valorrestante=valorrestante-50

    while valorrestante>=20:
        nota20=nota20+1
        valorrestante=valorrestante-20
    
    while valorrestante>=10:
        nota10=nota10+1
        valorrestante=valorrestante-10

    while valorrestante>=5:
        nota5=nota5+1
        valorrestante=valorrestante-5

    while valorrestante>=2:
        nota2=nota2+1
        valorrestante=valorrestante-2
    os.system("cls") #limpar terminal
    fim=1

print (" as notas a sacar são.")
# os "IF's" aqui, sao para aparecer no console apenas as notas que sairiam do caixa, omitindo as com valor 0.
if nota200>0:
    print (" notas de 200: ",nota200)

if nota100>0:
    print (" notas de 100: ",nota100)

if nota50>0:
    print (" notas de 50: ",nota50)

if nota20>0:
    print (" notas de 20: ",nota20)

if nota100>0:
    print (" notas de 10: ",nota10)

if nota5>0:
    print (" notas de 5: ",nota5)

if nota2>0:
    print (" notas de 2: ",nota2)

if valorrestante>0:
    print (" resto nao possivel de sacar: ",valorrestante) #nota de 1 real nao esta mais em circulaçao no brasil.

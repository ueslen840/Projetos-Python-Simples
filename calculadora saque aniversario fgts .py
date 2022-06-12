saldo = float (input("digite seu saldo do fgts. \n"))


# aqui sera feito o calculo para saldos ate 500 reais, onde o saque é de 50%
if saldo < 500.01:
    saque = saldo * 0.5
    restante = saldo - saque
    print ("seu saque sera de ", saque ," Reais e sobrará", restante," Reais")
# aqui o de ate 1000, sendo 40% de saque + 50 reais
elif saldo < 1000:
    saque = (saldo * 0.4) + 50
    restante = saldo - saque
    print ("seu saque sera de ", saque ," Reais e sobrará", restante," Reais")
# aqui o de ate 5000, sendo 30%+150
elif saldo < 5000:
    saque = (saldo * 0.3) + 150
    restante = saldo - saque
    print ("seu saque sera de ", saque ," Reais e sobrará", restante," Reais")
#aqui o de ate 10 mil, sendo 20%+650
elif saldo < 10000:
    saque = (saldo * 0.2) + 650
    restante = saldo - saque
    print ("seu saque sera de ", saque ," Reais e sobrará", restante," Reais")
# ate 15 mil, 15%+1150
elif saldo < 15000:
    saque = (saldo * 0.15) + 1150
    restante = saldo - saque
    print ("seu saque sera de ", saque ," Reais e sobrará", restante," Reais")
# 20 mil, 10%+1900
elif saldo < 20000:
    saque = (saldo * 0.1) + 1900
    restante = saldo - saque
    print ("seu saque sera de ", saque ," Reais e sobrará", restante," Reais")
# aqui o restante, qualquer valor acima de 20 mil 5%+2900
else:
    saque = (saldo * 0.05) + 2900
    restante = saldo - saque
    print ("seu saque sera de ", saque ," Reais e sobrará", restante," Reais")


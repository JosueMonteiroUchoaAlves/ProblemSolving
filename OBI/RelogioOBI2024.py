horas = int(input())
minutos = int(input())
segundos = int(input())
atraso = int(input())

segundos += atraso
minutos += (segundos // 60)
segundos = segundos % 60
horas += (minutos // 60)
horas = horas % 24
minutos = minutos % 60

print(horas, minutos ,segundos, sep=' ')

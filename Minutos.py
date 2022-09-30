import datetime

hora = datetime.datetime.now()
minutos_real = datetime.datetime.strftime(hora, '%M')
minutos_real = int(minutos_real)+1
print(minutos_real)

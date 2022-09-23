import datetime

fechaactual = datetime.datetime.now()
print(fechaactual)

fecha = datetime.datetime(2022, 10, 1)
fecha1 = datetime.datetime(2022, 10, 1, 23, 45)
print(fecha1)

fechaactual2 = datetime.datetime.strftime(fechaactual, '%d/%m/%Y %H:%M:%S')
print(fechaactual2)

fechaactual3 = datetime.datetime.strftime(fechaactual, '%b %d %Y %H:%M:%S')
print(fechaactual3)

fechaTexto = "Dec 06 2022 22:10"
fechaactual4 = datetime.datetime.strptime(fechaTexto, '%b %d %Y %H:%M')
print(fechaactual4)

dia = int(datetime.datetime.strftime(fechaactual, '%d'))
print(dia)

horaactual = datetime.datetime.strftime(fechaactual, '%H:%M:%S')
print(horaactual)

fechapasada = datetime.datetime(2022, 9, 1)
diferencia = fechaactual - fechapasada
print(diferencia)
print(diferencia.days)
print(diferencia.total_seconds())

dia_delta = datetime.timedelta(days=5)
fechainicial = datetime.date.today()
print(fechaactual)
fechafutura = fechainicial + dia_delta
print(fechafutura)

fecha5 = datetime.datetime.now().isoformat()
print(fecha5)
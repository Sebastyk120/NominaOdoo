import datetime

# from datetime import datetime

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

# Recolectar fecha de inicio y hora
fecha_hora_vacia = input("Ingrese la fecha y hora --- Ejemplo 17/03/2022 13:30: ")
fecha_hora_vacia2 = datetime.datetime.strptime(fecha_hora_vacia, '%d/%m/%Y %H:%M')
print(fecha_hora_vacia2)


def horainicio():
    fecha_nom_ijd = datetime.datetime(2022, 3, 26, 13, 30)
    hora = datetime.datetime.strftime(fecha_nom_ijd, '%H')
    hora = int(hora)
    minutos = datetime.datetime.strftime(fecha_nom_ijd, '%M')
    minutos = round(float(minutos) / 60, 1)
    horarioentrada = hora + minutos
    return horarioentrada


vacio = None
horainicio2 = horainicio()
print(horainicio2)
"""if horainicio != 0:
    if horainicio2 ==0 and horainicio2 == 1:"""

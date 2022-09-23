import datetime

"""----------------------------------------- Declaracion de variables -----------------------------------------------"""
jornada_ordinaria_horas = 8

"""-----------------------------------Recolectores De Floats Horas --------------------------------------------------"""

"""Recolectar fecha de inicio y hora"""


def hora_inicio_jornada():
    inicio_jornada_vacia = input("Ingrese la fecha y hora inicio jornada - Ejemplo 17/03/2022 13:30: ")
    inicio_jornada_vacia = datetime.datetime.strptime(inicio_jornada_vacia, '%d/%m/%Y %H:%M')
    hora_i = datetime.datetime.strftime(inicio_jornada_vacia, '%H')
    hora_i = int(hora_i)
    minutos = datetime.datetime.strftime(inicio_jornada_vacia, '%M')
    minutos = round(float(minutos) / 60, 1)
    horarioentrada = hora_i + minutos
    return horarioentrada, hora_i


i, hora_i_i = hora_inicio_jornada()

"""Recolectar fecha de inicio descanso y hora"""


def hora_inicio_descanso():
    inicio_descanso_vacia = input(
        "Ingrese la fecha y hora inicio descanso (Si no  hay descanso escriba N/A) - Ejemplo 17/03/2022 13:30: ")
    if inicio_descanso_vacia == "N/A":
        return inicio_descanso_vacia
    else:
        inicio_descanso_vacia = datetime.datetime.strptime(inicio_descanso_vacia, '%d/%m/%Y %H:%M')
        hora_i_d = datetime.datetime.strftime(inicio_descanso_vacia, '%H')
        hora_i_d = int(hora_i_d)
        minutos = datetime.datetime.strftime(inicio_descanso_vacia, '%M')
        minutos = round(float(minutos) / 60, 1)
        horario_entrada_descanso = hora_i_d + minutos
        return horario_entrada_descanso, hora_i_d


d, hora_i_d_d = hora_inicio_descanso()

"""Recolectar fecha de salida descanso y hora"""


def hora_salida_descanso():
    salida_descanso_vacia = input(
        "Ingrese la fecha y hora salida descanso (Si no  hay descanso escriba N/A)- Ejemplo 17/03/2022 13:30: ")
    if salida_descanso_vacia == "N/A":
        return salida_descanso_vacia
    else:
        salida_descanso_vacia = datetime.datetime.strptime(salida_descanso_vacia, '%d/%m/%Y %H:%M')
        hora_s_d = datetime.datetime.strftime(salida_descanso_vacia, '%H')
        hora_s_d = int(hora_s_d)
        minutos = datetime.datetime.strftime(salida_descanso_vacia, '%M')
        minutos = round(float(minutos) / 60, 1)
        salida_descanso_vacia = hora_s_d + minutos
        return salida_descanso_vacia, hora_s_d


r, hora_s_d_d = hora_salida_descanso()

"""Recolectar fecha de salida jornada y hora"""


def hora_salida_jornada():
    salida_jornada_vacia = input("Ingrese la fecha y hora salida jornada - Ejemplo 17/03/2022 13:30: ")
    salida_jornada_vacia = datetime.datetime.strptime(salida_jornada_vacia, '%d/%m/%Y %H:%M')
    hora_s = datetime.datetime.strftime(salida_jornada_vacia, '%H')
    hora_s = int(hora_s)
    minutos = datetime.datetime.strftime(salida_jornada_vacia, '%M')
    minutos = round(float(minutos) / 60, 1)
    salida_jornada_vacia = hora_s + minutos
    return salida_jornada_vacia, hora_s


s, hora_s_s = hora_salida_jornada()

"""-----------------------------------Funcion Ingreso A Descanso --------------------------------------------------"""


def laboradas_azul():
    if hora_i_d_d != "N/A" and hora_s_d_d != "N/A":
        if hora_i_d_d > hora_i_i:
            laboradas = hora_i_d_d - hora_i_i
            return laboradas
        else:
            if hora_i_d_d < hora_i_i:
                laboradas = 24 - hora_i_i + hora_i_d_d
                return laboradas
            else:
                laboradas = 0
                return laboradas
    else:
        laboradas = None
        return laboradas
laboradas2 = laboradas_azul()
print(laboradas2)


print("hola")

"""if horainicio != 0:
    if horainicio2 ==0 and horainicio2 == 1:"""

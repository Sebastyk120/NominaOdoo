from openpyxl import load_workbook
import pywhatkit
import datetime

# load excel file
path = ''
workbook = load_workbook(
    filename="C:/Users/SebastianM/HEAVEN/HeavensCorp - Documentos/HF Corp/Espacio de Trabajo/Gestion de COMPRAS/Adquisicion de fruta/Erp compras/ProgramacionTransporte.xlsx")

# open workbook
sheet = workbook.active

rango_condicion = sheet['A1':'AD500']
rango_Columna = sheet['AD1':'AD500']

contador = -1
contador2 = 1
ide = "id"
tipo_de_servicio = "tipo_de_servicio"
fecha_servicio = "tipo_de_servicio"
hora_servicio = "hora_servicio"
producto = "producto"
cantidad_producto = "cantidad_producto"
kilogramos = "kilogramos"
origen = "origen"
destino = "destino"
proveedor = "proveedor"
celular_proveedor = "celular_proveedor"
conductor = "conductor"
celular_conductor = "celular_conductor"

for i in rango_Columna:
    contador += 1
    contador2 += int(1)
    if i[0].value == "No Enviado":
        i[0].value = "Enviado"
        ide = str(rango_condicion[contador][0].value)
        tipo_de_servicio = rango_condicion[contador][5].value
        fecha_servicio = rango_condicion[contador][7].value
        hora_servicio = rango_condicion[contador][8].value
        producto = rango_condicion[contador][9].value
        cantidad_producto = rango_condicion[contador][10].value
        kg = rango_condicion[contador][11].value
        origen = rango_condicion[contador][12].value
        destino = rango_condicion[contador][13].value
        proveedor = str(rango_condicion[contador][14].value)
        celular_proveedor = rango_condicion[contador][15].value
        conductor = rango_condicion[contador][16].value
        celular_conductor = rango_condicion[contador][17].value
        telefono = "E2YLsn9pOxH52lBJZtPeC9"
        hora = datetime.datetime.now()
        hora_real = datetime.datetime.strftime(hora, '%H')
        hora_real = int(hora_real)
        minutos_real = datetime.datetime.strftime(hora, '%M')
        minutos_real = int(minutos_real)
        if minutos_real == 60:
            minutos_real = 1
        elif minutos_real >= 59:
            minutos_real = 1 + 1
        else:
            minutos_real = minutos_real + 1
        pywhatkit.sendwhatmsg_to_group(telefono, ide + '\n' + 'Boot de Prueba *Proveedor:* ' + proveedor, hora_real,
                                       minutos_real, 8, True, 4)
    else:
        print("programa terminado")

# modify he desired cell
# sheet["L6"] = "Ejecutado123"

# save the file
workbook.save(filename="C:/Users/SebastianM/HEAVEN/HeavensCorp - Documentos/HF Corp/Espacio de Trabajo/Gestion de COMPRAS/Adquisicion de fruta/Erp compras/ProgramacionTransporte.xlsx")

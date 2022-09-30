import datetime
import pywhatkit
from openpyxl import load_workbook
import locale
locale.setlocale(locale.LC_ALL, ("es_ES", "UTF-8"))

# load excel file
path = ''
workbook = load_workbook(
    filename="C:/Users/SebastianM/HEAVEN/HeavensCorp - Documentos/HF Corp/Espacio de Trabajo/Gestion de COMPRAS/Adquisicion de fruta/Erp compras/ProgramacionTransporte.xlsx")

# open workbook
sheet = workbook.active

rango_condicion = sheet['A1':'AD500']
rango_ide = sheet['A1':'A500']
rango_Columna = sheet['AD1':'AD500']

contador = -1
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
nombre_solicitud = "nombre_solicitud"
print(sheet["AD2"].value)

for i in rango_Columna:
    contador += 1
    if i[0].value is None and rango_condicion[contador][0].value is not None:
        ide = str(rango_condicion[contador][0].value)
        tipo_de_servicio = str(rango_condicion[contador][5].value)
        fecha_servicio = str(datetime.datetime.strftime(rango_condicion[contador][7].value, "%d-%B-%Y"))
        hora_servicio = str(rango_condicion[contador][8].value)
        producto = str(rango_condicion[contador][9].value)
        cantidad_producto = str(rango_condicion[contador][10].value)
        kg = str(rango_condicion[contador][11].value)
        origen = str(rango_condicion[contador][12].value)
        destino = str(rango_condicion[contador][13].value)
        proveedor = str(rango_condicion[contador][14].value)
        celular_proveedor = str(rango_condicion[contador][15].value)
        conductor = str(rango_condicion[contador][16].value)
        celular_conductor = str(rango_condicion[contador][17].value)
        nombre_solicitud = str(rango_condicion[contador][27].value)
        grupo_id = "E2YLsn9pOxH52lBJZtPeC9"
        hora = datetime.datetime.now()
        hora_real = datetime.datetime.strftime(hora, '%H')
        hora_real = int(hora_real)
        minutos_real = datetime.datetime.strftime(hora, '%M')
        minutos_real = int(minutos_real)
        if minutos_real == 59:
            minutos_real = 1
        else:
            minutos_real = minutos_real + 1
        pywhatkit.sendwhatmsg_to_group(grupo_id,
                                       '*Consecutivo:* ' + ide + '\n' + '*Tipo De Servicio:* ' + tipo_de_servicio + '\n' +
                                       '*Fecha Del Servicio:* ' + fecha_servicio + '\n' + '*Hora Del Servicio:* ' + hora_servicio + '\n' +
                                       '*Producto:* ' + producto + '\n' + '*Cantidad Producto:* ' + cantidad_producto + '\n' +
                                       '*Cantidad Kg:* ' + kg + '\n' + '*Origen:* ' + origen + '\n' +
                                       '*Destino:* ' + destino + '\n' + '*Proveedor:* ' + proveedor + '\n' + '*Celular Proveedor:* ' + celular_proveedor + '\n' +
                                       '*Conductor:* ' + conductor + '\n' + '*Celular Conductor:* ' + celular_conductor + '\n' + '*Solicitante:* ' + nombre_solicitud,
                                       hora_real,
                                       minutos_real, 8, True, 2)
        i[0].value = "Enviado"
    else:
        print(' Mensaje enviado')

# modify he desired cell
# sheet["L6"] = "Ejecutado123"

# save the file
workbook.save(
    filename="C:/Users/SebastianM/HEAVEN/HeavensCorp - Documentos/HF Corp/Espacio de Trabajo/Gestion de COMPRAS/Adquisicion de fruta/Erp compras/ProgramacionTransporte.xlsx")
quit()

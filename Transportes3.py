from openpyxl import load_workbook
import pywhatkit

# load excel file
path = ''
workbook = load_workbook(filename="ProgramacionTransporte.xlsx")

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
    contador2 += 1
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
        telefono = "F5dON49gKSRLedCuPjuGye"
        pywhatkit.sendwhatmsg_to_group(telefono, ide + '\n' + '*Boot de Prueba Proveedor:* ' + proveedor, 22, 24, 8, True, 4)
    else:
        print("programa terminado")

# modify he desired cell
# sheet["L6"] = "Ejecutado123"

# save the file
workbook.save(filename="ProgramacionTransporte.xlsx")

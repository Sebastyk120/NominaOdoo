from openpyxl import load_workbook

# load excel file
workbook = load_workbook(filename="ProgramacionTransporte.xlsx")

# open workbook
sheet = workbook.active

rango_condicion = sheet['A1':'M308']
rango_Columna = sheet['L1':'L308']

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


for i in rango_Columna:
    contador += 1
    if i[0].value == "Hola":
        i[0].value = "Hola"
        ide = rango_condicion[contador][0].value
        tipo_de_servicio = rango_condicion[contador][5].value
        fecha_servicio = rango_condicion[contador][7].value
        hora_servicio = rango_condicion[contador][8].value
        producto = rango_condicion[contador][9].value
        cantidad_producto = rango_condicion[contador][10].value
        kilogramos = rango_condicion[contador][11].value
        origen = rango_condicion[contador][12].value
        destino = rango_condicion[contador][13].value
        proveedor = rango_condicion[contador][14].value
        celular_proveedor = rango_condicion[contador][15].value
        conductor = rango_condicion[contador][16].value
        celular_conductor = rango_condicion[contador][17].value

# modify he desired cell
# sheet["L6"] = "Ejecutado123"

# save the file
workbook.save(filename="ProgramacionTransporte.xlsx")

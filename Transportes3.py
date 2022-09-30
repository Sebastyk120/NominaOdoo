from openpyxl import load_workbook

# load excel file
workbook = load_workbook(filename="ProgramacionTransporte.xlsx")

# open workbook
sheet = workbook.active

Rango_condicion = sheet['A1':'M308']
rango_Columna = sheet['L1':'L308']

contador = -1
Proveedor = "Proveedor"
Nombre = "Nombre"


for i in rango_Columna:
    contador += 1
    if i[0].value == "Hola":
        i[0].value = "Hola"
        Proveedor = Rango_condicion[contador][12].value
        Nombre = Rango_condicion[contador][14].value

# modify he desired cell
# sheet["L6"] = "Ejecutado123"

# save the file
workbook.save(filename="ProgramacionTransporte.xlsx")

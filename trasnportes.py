import numpy as np
import pandas as pd
<<<<<<< HEAD
=======
import xlsxwriter
>>>>>>> 6988272 (Se añaden declaraciones de horas flotantes.)
import openpyxl

# Lectura del archivo .xlsx

<<<<<<< HEAD
transportes_df = pd.read_excel('ProgramaciónTransporte.xlsx',sheet_name='Resultado')

# Mostrar libro

#transportes_df['salida'] = transportes_df.mean(axis=1)
=======
transportes_df = pd.read_excel('ProgramacionTransporte.xlsx', sheet_name='Resultado2', index_col=None,
                               engine='openpyxl')

# Mostrar libro

# transportes_df['salida'] = transportes_df.mean(axis=1)
>>>>>>> 6988272 (Se añaden declaraciones de horas flotantes.)

# transportes_df['Enviado'] = np.where(transportes_df['media'] >20, 'Ok', 'Nok')

condicion = [
    (transportes_df['Comprobador'] == 1),
    (transportes_df['Comprobador'] == 0),
]
notas = ['Ejecutado', 'No Ejecutado']

transportes_df['Ok'] = np.select(condicion, notas)
<<<<<<< HEAD

print(transportes_df)

transportes_df.to_excel(excel_writer='ProgramaciónTransporte.xlsx', sheet_name='Resultado2')



=======
print(transportes_df)
transportes_df.to_excel('ProgramacionTransporte.xlsx', sheet_name='Resultado2')
transportes_df.to_excel('ProgramacionTransporte.xlsx', sheet_name='Resultado2', engine='xlsxwriter')
>>>>>>> 6988272 (Se añaden declaraciones de horas flotantes.)

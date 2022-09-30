import numpy as np
import pandas as pd
import openpyxl

# Lectura del archivo .xlsx

transportes_df = pd.read_excel('ProgramaciónTransporte.xlsx',sheet_name='Resultado')

# Mostrar libro

#transportes_df['salida'] = transportes_df.mean(axis=1)

# transportes_df['Enviado'] = np.where(transportes_df['media'] >20, 'Ok', 'Nok')

condicion = [
    (transportes_df['Comprobador'] == 1),
    (transportes_df['Comprobador'] == 0),
]
notas = ['Ejecutado', 'No Ejecutado']

transportes_df['Ok'] = np.select(condicion, notas)

print(transportes_df)

transportes_df.to_excel(excel_writer='ProgramaciónTransporte.xlsx', sheet_name='Resultado2')




from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.file import File
import io
import pandas as pd

#target url taken from sharepoint and credentials
url = 'https://heaven0.sharepoint.com/sites/HeavensCorp/Documentos%20compartidos/HF%20Corp/Espacio%20de%20Trabajo/Gestion%20de%20COMPRAS/Adquisicion%20de%20fruta/Erp%20compras/ProgramacionTransporte.xlsx'
username = 'sebastian.melo@heavensfruit.com'
password = 'Password!'

ctx_auth = AuthenticationContext(url)
if ctx_auth.acquire_token_for_user(username, password):
  ctx = ClientContext(url, ctx_auth)
  web = ctx.web
  ctx.load(web)
  ctx.execute_query()
  print("Authentication successful")

response = File.open_binary(ctx, url)

#save data to BytesIO stream
bytes_file_obj = io.BytesIO()
bytes_file_obj.write(response.content)
bytes_file_obj.seek(0) #set file object to start

#read excel file and each sheet into pandas dataframe 
df = pd.read_excel(bytes_file_obj, sheetname = None)
import pandas as pd
from twilio.rest import Client

print('Nhaeeew!')

# Your Account SID from twilio.com/console
account_sid = "****"
# Your Auth Token from twilio.com/console
auth_token  = "****"

client_twilio = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mes de {mes} o vendedor: {vendedor} bateu a meta de: {vendas} vendas')
        message = client_twilio.messages.create(
            to="+5585991697027", 
            from_="+18326482439",
            body='Acorda pra cuspir rapaaaaaz!')

print(message.sid)
        





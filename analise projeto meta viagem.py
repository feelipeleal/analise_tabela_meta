#pandas
#openpyxl
#twilio

import pandas as pd
from twilio.rest import Client


# ID TWILION
account_sid = 'AC890b7270526db0dfbdeea04cd9267e4e'
# TOKEN TWILION
auth_token = '3e9d13a87ed1766348e5c2ed6ccbaf4a'
client = Client(account_sid, auth_token)

# passo a passo de solução

# abrir os 6 arquivos em excel
lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        Vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        Vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes}, alguém bateu a meta. Vendedor: {Vendedor} e suas Vendas: {Vendas}')
        # mensagem SMS
        message = client.messages \
                .create(
                     body=f'No mês de {mes}, alguém bateu a meta. Vendedor: {Vendedor} e suas Vendas: {Vendas}',
                     from_='+16413263946',
                     to='+5548996600343'
                 )

print(message.sid)

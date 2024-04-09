"""
Exercise - Resolving Problem

pt-br to be short

Maria pegou um empréstimo de 100.000 para realizar o pagamento
em 5 anos. A data em que ela pegou o empréstimo foi 20/10/2020
e o vencimento de cada parcela ocorre no dia 20 de cada mês.
- Criar data do empréstimo
- Criar data final do empréstimo
- Exibir todas as datas de vencimento e o valor de cada parcela
"""
from datetime import datetime
from dateutil.relativedelta import relativedelta

pattern = '%d/%m/%Y'

data_emprestimo = datetime.strptime('20/10/2020', pattern)
quantidade_anos = relativedelta(years=5)
data_final = data_emprestimo + quantidade_anos
valor_emprestimo = 100000

datas_parcelas = []

data_parcela = data_emprestimo

while data_parcela < data_final:
    datas_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=1)

for data in datas_parcelas:
    print(f'{data.strftime(pattern)} -{valor_emprestimo / datas_parcelas.__len__():.2f}')

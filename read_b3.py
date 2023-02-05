import pandas as pd

# Define posição das colunas cf.https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/cotacoes-historicas/
colspecs = [
    (0,2),
    (2,10),
    (10,12),
    (12,24),
    (24,27),
    (27,39),
    (39,49),
    (49,52),
    (52,56),
    (56,69),
    (69,82),
    (82,95),
    (95,108),
    (108,121),
    (121,134),
    (134,147),
    (147,152),
    (152,170),
    (170,188),
    (188,201),
    (201,202),
    (202,210),
    (210,217),
    (217,230),
    (230,242),
    (242,245)
    ]

# Define nomes das colunas cf. https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/cotacoes-historicas/
names = [
    'TIPGRE',
    'DATA_PREGAO',
    'CODBDI',
    'CODNEG',
    'TPMERC',
    'NOMRES',
    'ESPECI',
    'PRAZTOT',
    'MODREF',
    'PREABE',
    'PREMAX',
    'PREMIN',
    'PREMED',
    'PREULT',
    'PREOFC',
    'PREOFV',
    'TOTNEG',
    'QUATOT',
    'VOLTOT',
    'PREEXE',
    'INDOPC',
    'DATVEN',
    'FATCOT',
    'PTOEXE',
    'CODISI',
    'DISMES'
    ]

file = 'DemoCotacoesHistoricas12022003.txt'

b3 = pd.read_fwf(file,
                 colspecs=colspecs,
                 skiprows=1)[:-1]
b3.columns = names

# converte data do pregação para datetime
b3['DATA_PREGAO'] = pd.to_datetime(b3['DATA_PREGAO'])


import pandas as pd
import matplotlib.pyplot as plt

# Dados simulados (substitua por carregamento real dos CSVs da PNP)
""" data_matriculas = {
    'codigo_instituicao': [2850, 2850, 2850, 2850, 2850, 1234, 2850],  # Código do IFSC é tipicamente 2850 no SISTEC/PNP
    'sigla_instituicao': ['IFSC', 'IFSC', 'IFSC', 'IFSC', 'IFSC', 'IFRS', 'IFSC'],
    'nivel_ensino': ['Ensino Médio Integrado', 'Ensino Médio Integrado', 'Ensino Médio Integrado', 
                     'Ensino Médio Concomitante', 'Ensino Médio Integrado', 'Ensino Médio', 'Ensino Médio Integrado'],
    'eixo_tecnologico': ['Informação e Comunicação', 'Produção Alimentícia', 'Informação e Comunicação', 
                         'Gestão e Negócios', 'Informação e Comunicação', 'Gestão', 'Informação e Comunicação'],
    'sexo_aluno': ['Feminino', 'Feminino', 'Masculino', 'Feminino', 'Feminino', 'Feminino', 'Feminino'],
    'renda_familiar_per_capita': ['Até 0.5 SM', '0.5 a 1 SM', '1 a 1.5 SM', 'Até 0.5 SM', 
                                  '1 a 1.5 SM', 'Até 0.5 SM', 'Acima de 3 SM'],
    'situacao_matricula_inicial': ['Ativa', 'Ativa', 'Ativa', 'Ativa', 'Ativa', 'Ativa', 'Ativa'],
    'situacao_matricula_final': ['Evadida', 'Concluída', 'Ativa', 'Evadida', 'Concluída', 'Evadida', 'Concluída']
}

df = pd.DataFrame(data_matriculas) """

df = pd.read_csv('microdados_eficiencia_academica_2020.csv', sep=';')

# Filtragem principal
# 1. Apenas IFSC
df_ifsc = df[df['Instituição'] == 'IFSC']

# 2. Ensino médio (integrado ou concomitante - cursos técnicos associados ao EM)
df_em = df_ifsc[df_ifsc['Tipo de Oferta'].str.contains('Integrado|Subsequente')]

# 3. Cursos tecnológicos (eixos como Informação, Produção, Gestão etc. - exclua 'Infraestrutura', 'Ambiente' etc. se necessário)
cursos_tecnologicos = ['Informação e Comunicação', 'Informática', 'Gestão e Negócios', 'Mecânica']  # Exemplos comuns
df_tec = df_em[df_em['Eixo Tecnológico'].isin(cursos_tecnologicos)]

# 4. Apenas meninas
df_meninas = df_tec[df_tec['Sexo'] == 'F']

# Cálculo de evasão por faixa de renda
# Considera evasão se situação final for 'Evadida', 'Cancelada', 'Desistente' etc. (no real, use códigos exatos do dicionário)
df_meninas['evadida'] = df_meninas['Situação de Matrícula'].str.contains('Abandono', case=False)

evasao_por_renda = (
    df_meninas.groupby('Renda Familiar')
    .agg(
        total_matriculas=('evadida', 'size'),
        evadidas=('evadida', 'sum')
    )
    .reset_index()
)

evasao_por_renda['taxa_evasao_%'] = (evasao_por_renda['evadidas'] / evasao_por_renda['total_matriculas'] * 100).round(2)

print("Taxa de evasão de meninas em cursos tecnológicos do ensino médio no IFSC, por renda:")
print(evasao_por_renda)

# Visualização simples (gráfico de barras)
evasao_por_renda.plot(kind='bar', x='Renda Familiar', y='taxa_evasao_%', title='Taxa de Evasão (%) por Faixa de Renda')
plt.ylabel('Taxa de Evasão (%)')
plt.xlabel('Renda Familiar per Capita')
plt.show()
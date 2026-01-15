import pandas as pd

from grafico1 import grafico_evasao_por_renda
from grafico2 import grafico_evasao_renda
from grafico3 import grafico_matricula_evasao_por_renda

anos = [2019, 2020, 2021, 2022, 2023]
lista_df = []

for ano in anos:
    df = pd.read_csv(
        f"dados/microdados_eficiencia_academica_{ano}.csv",
        sep=";",
        encoding="utf-8-sig",
        low_memory=False
    )
    
    df["ANO_REFERENCIA"] = ano
    lista_df.append(df)

df = pd.concat(lista_df, ignore_index=True)

print(df["ANO_REFERENCIA"].value_counts())

# Filtrar IFSC - Documentação informa que na coluna "Instituição" informa a sigla do Câmpus mas no arquivo de 2023 está por extenso 
df = df[
    df["Instituição"].str.contains(
        "IFSC|Instituto Federal de Santa Catarina",
        case=False,
        na=False
    )
]

#Ensino Médio Técnico Integrado ou técnicos concomitante e subsequente
df = df[
    df["Tipo de Oferta"].str.contains(
        "Integrado|Concomitante|Subsequente",
        case=False,
        na=False
    )
]

#Na PNP os cursos são subdivididos por eixos e as nomenclaturas são criadas para a plataforma então decidi filtrar apenas pelo eixo tecnológico onde está os cursos de informática
df = df[
    df["Eixo Tecnológico"].str.contains(
        "Informação e Comunicação",
        case=False,
        na=False
    )
]

#Coletar dados por sexo
df_fem = df[df["Sexo"] == "F"].copy()
df_masc = df[df["Sexo"] == "M"].copy()

#meninas
df_fem["EVASAO"] = df_fem["Situação de Matrícula"].isin(
    ["Abandono", "Desligada"]
)

#meninos
df_masc["EVASAO"] = df_masc["Situação de Matrícula"].isin(
    ["Abandono", "Desligada"]
)

#evasão feminina / ano
evasao_fem_ano = (
    df_fem
    .groupby("ANO_REFERENCIA")
    .agg(
        total_matriculas=("EVASAO", "count"),
        total_evasoes=("EVASAO", "sum")
    )
)

evasao_fem_ano["taxa_evasao_%"] = (
    evasao_fem_ano["total_evasoes"] /
    evasao_fem_ano["total_matriculas"] * 100
).round(2)

print(evasao_fem_ano)



#evasao feminina /  renda /  ano
evasao_fem_renda_ano = (
    df_fem
    .groupby(["ANO_REFERENCIA", "Renda Familiar"])
    .agg(
        total_matriculas=("EVASAO", "count"),
        total_evasoes=("EVASAO", "sum")
    )
)

evasao_fem_renda_ano["taxa_evasao_%"] = (
    evasao_fem_renda_ano["total_evasoes"] /
    evasao_fem_renda_ano["total_matriculas"] * 100
).round(2)

print(evasao_fem_renda_ano)

#comparação
evasao_sexo_ano = (
    pd.concat([
        df_fem.assign(SEXO="F"),
        df_masc.assign(SEXO="M")
    ])
    .groupby(["ANO_REFERENCIA", "SEXO"])
    .agg(
        total_matriculas=("EVASAO", "count"),
        total_evasoes=("EVASAO", "sum")
    )
)

evasao_sexo_ano["taxa_evasao_%"] = (
    evasao_sexo_ano["total_evasoes"] /
    evasao_sexo_ano["total_matriculas"] * 100
).round(2)

print(evasao_sexo_ano)

# Gráficos
grafico_evasao_por_renda(df_fem)
grafico_evasao_renda(df_fem)
grafico_matricula_evasao_por_renda(df_fem)

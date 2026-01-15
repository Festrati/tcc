

""" Eixo Tecnológico - Eixo tecnológico do curso associado pela instituição na PNP
Instituição - Sigla da Instituição na PNP. Cada escola técnica vinculada às Universidades Federais foi compreendida como uma Instituição
Modalidade de Ensino Classificação para identificar ensino presencial ou ensino a distância. 
Renda Familiar - Faixa de renda per capita familiar do aluno, declara na PNP pela instituição (Opções: 0<RFP<=0,5; 0,5<RFP<=1; 1<RFP<=1,5;1,5<RFP<=2,5; 2,5<RFP<=3,5; RFP>3,5; Não declarada).
Sexo - Informa o sexo do estudante constante no SISTEC. 
Situação da Matrícula - Atributo que apresenta a situação da matrícula do aluno conforme declarado/validado na PNP.
A situação inicial damatricula é “Em Curso”. As situações possíveis são:
Em Curso: matrícula ativa.
Cancelada: aplica-se ao aluno que solicita formalmente o cancelamento da sua matrícula antes de iniciar as atividades pedagógicas do curso.
Abandono: aplica-se ao aluno que possui mais de 25% de faltas não justificadas. Recomenda-se se modificar o status para “Abandono” somente quando não houver mais possibilidade de o aluno voltar a frequentar as aulas.
Concluída: aplica-se ao aluno que concluiu todo o curso com êxito.
Desligada: aplica-se ao aluno que solicita formalmente o cancelamento da sua matrícula após iniciar as atividades pedagógicas do curso.
Integralizada: aplica-se ao aluno que concluiu a parte teórica do curso, mas está devendo o estágio obrigatório, TCC, monografia, dissertação ou tese.
Reprovada: O aluno finalizou o curso, porém não logrou êxito nas avaliações. Aplica-se nos casos de impossibilidade de continuação do curso.
Transf_ext: aplica-se ao aluno que será transferido para outra Unidade de Ensino.
Transf_int: aplica-se ao aluno que muda de curso, dentro da mesma Unidade de Ensino.
O campo foi validado/atualizado pela instituição na PNP.
Tipo Oferta - Categorização transversal utilizada para diferenciar as formas de oferta dos Cursos Técnicos e de Qualificação Profissional (FIC).
Opções: Integrado, Subsequente, Concomitante, PROEJA (Concomitante e PROEJA), PROEJA Integrado """

import pandas as pd

df = pd.read_csv(
    "microdados_eficiencia_academica_2023.csv",
    sep=";",
    encoding="utf-8-sig",
    low_memory=False
)

print(df.columns)
print(df["Situação de Matrícula"].value_counts())


#Filtrar IFSC - Documentação informa que na coluna "Instituição" informa a sigla do Câmpus mas no arquivo de 2023 está por extenso 
df_ifsc = df[
    df["Instituição"].str.contains(
        "IFSC|Instituto Federal de Santa Catarina",
        case=False,
        na=False
    )
]

#Ensino Médio Técnico Integrado ou técnicos concomitante e subsequente
df_em = df_ifsc[
    df_ifsc["Tipo de Oferta"].str.contains("Integrado|Concomitante|Subsequente", case=False, na=False)
]

#Na PNP os cursos são subdivididos por eixos e as nomenclaturas são criadas para a plataforma então decidi filtrar apenas pelo eixo tecnológico onde está os cursos de informática
df_em = df_em[
    df_em["Eixo Tecnológico"].str.contains(
        "Informação e Comunicação",
        case=False,
        na=False
    )
]

#Filtro para coletar dados por sexo
df_fem = df_em[df_em["Sexo"] == "F"]
df_masc = df_em[df_em["Sexo"] == "M"]


#Na PNP temos a coluna "Categoria da Situação" que já informa se a matricula está com status de evasão, como a PNP inclui os status Abandono, Desligada e Cancelada, eu decidi usar a coluna "Situação de Matrícula" pois assim eu retiro o status Cancelada que não corresponde ao estudo. 
#meninas
df_fem = df_fem.copy()
df_fem["EVASAO"] = df_fem["Situação de Matrícula"].isin(
    ["Abandono", "Desligada"]
)

#meninos
df_masc = df_masc.copy()
df_masc["EVASAO"] = df_masc["Situação de Matrícula"].isin(
    ["Abandono", "Desligada"]
)

#Cálculo por renda
#Meninas
evasao_fem = (
    df_fem
    .groupby("Renda Familiar")
    .agg(
        total_matriculas=("EVASAO", "count"),
        total_evasoes=("EVASAO", "sum")
    )
)

#Meninos
evasao_masc = (
    df_masc
    .groupby("Renda Familiar")
    .agg(
        total_matriculas=("EVASAO", "count"),
        total_evasoes=("EVASAO", "sum")
    )
)


evasao_fem["taxa_evasao_%"] = (
    evasao_fem["total_evasoes"] / evasao_fem["total_matriculas"] * 100
).round(2)

evasao_masc["taxa_evasao_%"] = (
    evasao_masc["total_evasoes"] / evasao_masc["total_matriculas"] * 100
).round(2)

print(evasao_fem)
print(evasao_masc)
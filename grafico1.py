import pandas as pd
import matplotlib.pyplot as plt

def grafico_evasao_por_renda(df_fem):
    ordem_renda = [
        "0<RFP<=0,5",
        "0,5<RFP<=1",
        "1<RFP<=1,5",
        "1,5<RFP<=2,5",
        "2,5<RFP<=3,5"
    ]

    agrupado = (
        df_fem
        .groupby(["ANO_REFERENCIA", "Renda Familiar"])
        .agg(
            total_matriculas=("EVASAO", "count"),
            total_evasoes=("EVASAO", "sum")
        )
        .reset_index()
    )

    agrupado["taxa_evasao"] = (
        agrupado["total_evasoes"] /
        agrupado["total_matriculas"] * 100
    )

    agrupado = agrupado[
        agrupado["Renda Familiar"].isin(ordem_renda)
    ]

    agrupado["Renda Familiar"] = pd.Categorical(
        agrupado["Renda Familiar"],
        categories=ordem_renda,
        ordered=True
    )

    plt.figure(figsize=(10,6))

    for renda in ordem_renda:
        dados = agrupado[agrupado["Renda Familiar"] == renda]
        plt.plot(
            dados["ANO_REFERENCIA"],
            dados["taxa_evasao"],
            marker="o",
            label=renda
        )

    plt.xlabel("Ano")
    plt.ylabel("Taxa de evasão feminina (%)")
    plt.title("Taxa de evasão feminina em cursos STEM por renda familiar (IFSC)")
    plt.legend(title="Renda Familiar")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

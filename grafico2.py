import pandas as pd
import matplotlib.pyplot as plt

# ======================
# Gráfico: Evasão feminina (%) por renda familiar
# ======================

def grafico_evasao_renda(df_fem):
    ordem_renda = [
        "0<RFP<=0,5",
        "0,5<RFP<=1",
        "1<RFP<=1,5",
        "1,5<RFP<=2,5",
        "2,5<RFP<=3,5"
    ]

    agrupado = (
        df_fem
        .groupby("Renda Familiar")
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

    agrupado = agrupado.sort_values("Renda Familiar")

    plt.figure(figsize=(8,6))

    plt.barh(
        agrupado["Renda Familiar"],
        agrupado["taxa_evasao"]
    )

    plt.xlabel("Taxa de evasão feminina (%)")
    plt.ylabel("Renda familiar")
    plt.title("Taxa de evasão feminina em cursos STEM por faixa de renda (IFSC)")
    plt.grid(axis="x")
    plt.tight_layout()
    plt.show()

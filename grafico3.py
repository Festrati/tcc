import pandas as pd
import matplotlib.pyplot as plt

# ======================
# Gráfico: Evasão feminina (%) por renda familiar
# ======================

   
def grafico_matricula_evasao_por_renda(df_fem):

    ordem_renda = [
        "0<RFP<=0,5",
        "0,5<RFP<=1",
        "1<RFP<=1,5",
        "1,5<RFP<=2,5",
        "2,5<RFP<=3,5"
    ]

    # ======================
    # Agrupamento geral por renda
    # ======================
    agrupado = (
        df_fem
        .groupby("Renda Familiar")
        .agg(
            total_matriculas=("EVASAO", "count"),
            total_evasoes=("EVASAO", "sum")
        )
        .reset_index()
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

    agrupado["taxa_evasao"] = (
        agrupado["total_evasoes"] /
        agrupado["total_matriculas"] * 100
    )

    # ======================
    # Gráficos lado a lado
    # ======================
    fig, axes = plt.subplots(1, 2, figsize=(12,6), sharey=True)

    # Gráfico 1 — Matrículas
    axes[0].barh(
        agrupado["Renda Familiar"],
        agrupado["total_matriculas"]
    )
    axes[0].set_title("Matrículas femininas em STEM")
    axes[0].set_xlabel("Número de matrículas")
    axes[0].set_ylabel("Renda familiar")
    axes[0].grid(axis="x")

    # Gráfico 2 — Evasão
    axes[1].barh(
        agrupado["Renda Familiar"],
        agrupado["taxa_evasao"]
    )
    axes[1].set_title("Taxa de evasão feminina (%)")
    axes[1].set_xlabel("Taxa de evasão (%)")
    axes[1].grid(axis="x")

    plt.suptitle(
        "Matrículas e evasão feminina em cursos STEM por renda familiar (IFSC)",
        fontsize=14
    )

    plt.tight_layout()
    plt.show()
   
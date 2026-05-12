import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# =========================
# DATOS
# =========================

empresa = pd.DataFrame({
    "Micro": [0.95],
    "Pequeña": [0.80],
    "Mediana": [0.40],
    "Grande": [0.05]
}, index=["Exclusión"])

ruralidad = pd.DataFrame({
    "Rural": [0.85],
    "Urbano": [0.30]
}, index=["Exclusión"])

ocupacion = pd.DataFrame({
    "Independiente": [0.90],
    "Asalariado": [0.25]
}, index=["Exclusión"])

region = pd.DataFrame({
    "Periferica": [0.80],
    "Intermedia": [0.50],
    "Bogota": [0.20]
}, index=["Exclusión"])

# =========================
# HEATMAPS INDIVIDUALES
# =========================

fig, axes = plt.subplots(2, 2, figsize=(12, 6))

sns.heatmap(empresa, annot=True, cmap="Reds", vmin=0, vmax=1, ax=axes[0,0])
axes[0,0].set_title("Tamaño de empresa")

sns.heatmap(ruralidad, annot=True, cmap="Reds", vmin=0, vmax=1, ax=axes[0,1])
axes[0,1].set_title("Ruralidad")

sns.heatmap(ocupacion, annot=True, cmap="Reds", vmin=0, vmax=1, ax=axes[1,0])
axes[1,0].set_title("Tipo de ocupación")

sns.heatmap(region, annot=True, cmap="Reds", vmin=0, vmax=1, ax=axes[1,1])
axes[1,1].set_title("Región")

plt.tight_layout()
plt.show()
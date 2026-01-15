import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.diagnostic import het_breuschpagan
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl as opxl

FILE_DESCRIPTIVE = 'DatosOriginales.xlsx' 
FILE_REGRESSION = 'CasoAerolineasDatos.csv'

try:
    print("Cargando bases de datos...")
    df_desc = pd.read_excel(FILE_DESCRIPTIVE)
    df_reg = pd.read_csv(FILE_REGRESSION)
    print("¡Datos cargados correctamente!\n")
except FileNotFoundError:
    print("Error: No se encontraron los archivos CSV. Verifica los nombres.")
    exit()

print("="*40)
print("       ANÁLISIS DESCRIPTIVO")
print("="*40)

print("\n--- Estadísticas de Precio ---")
print(df_desc['Ticket Price'].describe())

print("\n--- Distribución por Aerolínea (%) ---")
print(df_desc['Airline'].value_counts(normalize=True) * 100)

print("\n--- Distribución por Clase (%) ---")
print(df_desc['Fare Type'].value_counts(normalize=True) * 100)

print("\n" + "="*40)
print("    ANÁLISIS DE MULTICOLINEALIDAD")
print("="*40)

Y = df_reg['Ticket Price']
X = df_reg.drop(columns=['Ticket Price'])
X = sm.add_constant(X) 

vif_data = pd.DataFrame()
vif_data["Variable"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

print("\nFactor de Inflación de la Varianza (VIF):")
print(vif_data)
print("\nNota: Un VIF > 10 indica alta multicolinealidad (revisar 'Trips').")

print("\n" + "="*40)
print("      MODELO DE REGRESIÓN LINEAL")
print("="*40)

model = sm.OLS(Y, X).fit()
print(model.summary())

print("\n" + "="*40)
print("     VALIDACIÓN DE SUPUESTOS")
print("="*40)

residuals = model.resid
fitted_vals = model.fittedvalues

shapiro_stat, shapiro_p = stats.shapiro(residuals)
print(f"Prueba Shapiro-Wilk: p-value = {shapiro_p:.4f}")
if shapiro_p > 0.05:
    print("-> Se ACEPTA la Normalidad de los errores.")
else:
    print("-> Se RECHAZA la Normalidad (Alerta).")

bp_test = het_breuschpagan(residuals, model.model.exog)
bp_p = bp_test[1]
print(f"Prueba Breusch-Pagan: p-value = {bp_p:.6f}")
if bp_p > 0.05:
    print("-> Varianza Constante (Homocedasticidad).")
else:
    print("-> Varianza No Constante (Heterocedasticidad).")

print("\nGenerando gráficos de validación...")

sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

sns.histplot(residuals, kde=True, ax=axes[0], color='skyblue')
axes[0].set_title('Distribución de Residuales (Normalidad)')
axes[0].set_xlabel('Error')

sm.qqplot(residuals, line='45', fit=True, ax=axes[1])
axes[1].set_title('Q-Q Plot')

axes[2].scatter(fitted_vals, residuals, alpha=0.6, color='green')
axes[2].axhline(y=0, color='red', linestyle='--')
axes[2].set_title('Residuales vs. Predichos (Homocedasticidad)')
axes[2].set_xlabel('Precio Predicho')
axes[2].set_ylabel('Residuales')

plt.tight_layout()
plt.show()
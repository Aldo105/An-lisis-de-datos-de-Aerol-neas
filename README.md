# ✈️ Proyecto de Análisis de Datos: Predicción de Precios en Aerolíneas

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Finalizado-success)
![Data Science](https://img.shields.io/badge/Area-Data%20Science-orange)

## 📋 Descripción del Proyecto
Este proyecto consiste en un análisis estadístico exhaustivo y modelado predictivo sobre el comportamiento de precios en el servicio de transporte aéreo. Utilizando técnicas de **Regresión Lineal Múltiple** en Python, se identificaron las variables clave que determinan el costo de un boleto y se validaron supuestos estadísticos rigurosos.

El objetivo principal fue construir un modelo matemático capaz de predecir el precio de venta y entender el comportamiento del consumidor.

## 🛠️ Tecnologías Utilizadas
* **Python**: Lenguaje principal.
* **Pandas & NumPy**: Manipulación y limpieza de datos.
* **Statsmodels**: Modelado estadístico y pruebas de hipótesis (OLS).
* **Matplotlib & Seaborn**: Visualización de datos y diagnóstico de residuales.

---

## 📊 Hallazgos Clave: Comportamiento del Mercado
Tras realizar un análisis descriptivo de los datos, se detectaron 5 patrones fundamentales:

1.  **Dominio del Mercado Premium:** El **50% de las reservas** analizadas corresponden a *Primera Clase*, indicando una muestra con alta disposición a pagar.
2.  **Alta Variabilidad de Precios:** El precio promedio es de **$376 USD**, con un rango oscilante entre $300 y $620 dependiendo de las condiciones de compra.
3.  **Ventana de Compra:** Los usuarios compran con un promedio de **45 días de anticipación** (rango: 8 a 123 días).
4.  **Cuota de Mercado:** **American Airlines** lidera la preferencia (30.6%), seguida de Southwest y United.
5.  **Perfil del Viajero:** El 43.5% de los usuarios son viajeros "Casuales", mientras que los viajeros frecuentes representan una minoría.

---

## 📈 Metodología y Modelado

### 1. Análisis de Multicolinealidad (VIF)
Se evaluó la redundancia entre variables mediante el *Variance Inflation Factor*.
* **Alerta:** Se detectó multicolinealidad severa en la variable `Trips` (VIF > 14), lo que sugiere que está altamente correlacionada con el tipo de viajero.

### 2. Ecuación del Modelo Matemático
El modelo generado explica el **63.9% ($R^2$)** de la variación en los precios. La ecuación resultante es:

$$
Precio = 239.72 + 167.77(AA) + 143.81(Delta) + 176.75(United) - 0.40(Dias) + 84.35(FirstClass) - 33.69(Business)
$$

**Interpretación:**
* **Aerolíneas:** Volar con United o AA incrementa el precio base significativamente.
* **Anticipación:** Se ahorra **$0.40 USD** por cada día extra de anticipación.
* **Clase:** La *Primera Clase* aumenta el costo en **$84.35 USD** promedio.

---

## 🧪 Validación de Supuestos Estadísticos

Para asegurar la robustez del modelo, se realizaron pruebas de diagnóstico visual y numérico:

### A. Normalidad de los Errores
> **Prueba Shapiro-Wilk:** p-value = 0.389 (Se acepta Normalidad).

El histograma y el gráfico Q-Q confirman que los residuales siguen una distribución normal, validando las pruebas de hipótesis del modelo.

![Gráfico de Normalidad](ruta/a/tu/imagen_histograma_qq.png)
*(Asegúrate de subir tu imagen y poner la ruta correcta aquí)*

### B. Homocedasticidad (Varianza Constante)
> **Prueba Breusch-Pagan:** p-value < 0.05 (Existe Heterocedasticidad).

Se observa cierta dispersión en forma de "embudo" en los precios más altos. Esto indica que el modelo es muy preciso para tarifas estándar, pero tiene mayor margen de error en boletos de muy alto costo.

![Gráfico de Residuales](ruta/a/tu/imagen_residuales.png)

---

## 🚀 Cómo ejecutar este proyecto

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)

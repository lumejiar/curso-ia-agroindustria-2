import pandas as pd

# Cargar el dataset
df = pd.read_csv('datos_sensores.csv')

print("="*50)
print("ANÁLISIS DEL DATASET DATOS_SENSORES.CSV")
print("="*50)

# 1. Exploración Categórica
print("\n1. EXPLORACIÓN CATEGÓRICA")
print("-"*50)
conteo_especies = df['species'].value_counts()
print(conteo_especies)

# 2. Conteo Total
print("\n2. CONTEO TOTAL")
print("-"*50)
print(f"Total de registros: {len(df)}")
print(f"Dimensiones: {df.shape}")
print(f"Valores faltantes: {df.isnull().sum().sum()}")

# 3. Filtrado Numérico
print("\n3. FILTRADO NUMÉRICO")
print("-"*50)
flores_petal_largo = df[df['petal_length'] > 1.5]
print(f"Flores con petal_length > 1.5: {len(flores_petal_largo)}")

# 4. Detección de Outliers
print("\n4. DETECCIÓN DE OUTLIERS")
print("-"*50)
top_3 = df.nlargest(3, 'sepal_width')
print("Top 3 flores con mayor sepal_width:")
print(top_3[['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']])

print("\n" + "="*50)
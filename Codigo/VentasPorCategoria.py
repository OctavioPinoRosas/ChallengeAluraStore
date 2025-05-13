import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url1 = r"base-de-datos-challenge1-latam\tienda_1.csv"
url2 = r"base-de-datos-challenge1-latam\tienda_2.csv"
url3 = r"base-de-datos-challenge1-latam\tienda_3.csv"
url4 = r"base-de-datos-challenge1-latam\tienda_4.csv"

tienda1 = pd.read_csv(url1)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

# Convert 'Fecha de Compra' to datetime in all DataFrames
tienda1['Fecha de Compra'] = pd.to_datetime(tienda1['Fecha de Compra'], format='%d/%m/%Y')
tienda2['Fecha de Compra'] = pd.to_datetime(tienda2['Fecha de Compra'], format='%d/%m/%Y')
tienda3['Fecha de Compra'] = pd.to_datetime(tienda3['Fecha de Compra'], format='%d/%m/%Y')
tienda4['Fecha de Compra'] = pd.to_datetime(tienda4['Fecha de Compra'], format='%d/%m/%Y')

conteoCategoriaT1 = tienda1['Categoría del Producto'].value_counts()
conteoCategoriaT2 = tienda2['Categoría del Producto'].value_counts()
conteoCategoriaT3 = tienda3['Categoría del Producto'].value_counts()
conteoCategoriaT4 = tienda4['Categoría del Producto'].value_counts()
conteosCategorias = pd.DataFrame({
    'Tienda 1': conteoCategoriaT1,
    'Tienda 2': conteoCategoriaT2,
    'Tienda 3': conteoCategoriaT3,
    'Tienda 4': conteoCategoriaT4
})
conteosCategorias = conteosCategorias.fillna(0)
# Sumar los conteos de todas las tiendas
conteosCategorias['Total'] = conteosCategorias.sum(axis=1)

# Ordenar por 'Total' de mayor a menor
conteosOrdenado = conteosCategorias.sort_values(by='Total', ascending=False)

# Seleccionar las 5 categorías con más cantidad
top = conteosOrdenado.head(5)
# mostrar las 3 categorias mas vendidas
print(top)

# Ventas por categoria segun el valor monetario
# Paso 1: Obtener las categorías top (ya ordenadas por cantidad vendida)
categorias_top = top.index

# Paso 2: Filtrar los dataframes por esas categorías
ventasT1 = tienda1[tienda1['Categoría del Producto'].isin(categorias_top)]
ventasT2 = tienda2[tienda2['Categoría del Producto'].isin(categorias_top)]
ventasT3 = tienda3[tienda3['Categoría del Producto'].isin(categorias_top)]
ventasT4 = tienda4[tienda4['Categoría del Producto'].isin(categorias_top)]

# Paso 3: Agrupar por categoría y sumar los valores vendidos
valorT1 = ventasT1.groupby('Categoría del Producto')['Precio'].sum()
valorT2 = ventasT2.groupby('Categoría del Producto')['Precio'].sum()
valorT3 = ventasT3.groupby('Categoría del Producto')['Precio'].sum()
valorT4 = ventasT4.groupby('Categoría del Producto')['Precio'].sum()

# Paso 4: Crear DataFrame con el valor total por tienda y categoría
valores_top_categorias = pd.DataFrame({
    'Tienda 1': valorT1,
    'Tienda 2': valorT2,
    'Tienda 3': valorT3,
    'Tienda 4': valorT4
}).fillna(0)

# Agregar columna con total general por categoría
valores_top_categorias['Total'] = valores_top_categorias.sum(axis=1)

# mostrar las categorias mas vendidas segun el valor monetario
print(valores_top_categorias)

# Grafica de ventas por categoria
categorias = top.index.tolist()  # ['Muebles', 'Electrónicos', 'Juguetes']
tienda1Top = top['Tienda 1'].tolist()
tienda2Top = top['Tienda 2'].tolist()
tienda3Top = top['Tienda 3'].tolist()
tienda4Top = top['Tienda 4'].tolist()
# Número de categorías
n_categorias = len(categorias)
indice = np.arange(n_categorias)  # posiciones: 0, 1, 2
ancho = 0.2  # Ancho de cada barra

# Crear la gráfica
plt.figure(figsize=(12,6))

# Dibujar una barra para cada tienda
plt.bar(indice - 1.5*ancho, tienda1Top, width=ancho, label='Tienda 1')
plt.bar(indice - 0.5*ancho, tienda2Top, width=ancho, label='Tienda 2')
plt.bar(indice + 0.5*ancho, tienda3Top, width=ancho, label='Tienda 3')
plt.bar(indice + 1.5*ancho, tienda4Top, width=ancho, label='Tienda 4')

# Configurar etiquetas
plt.xlabel('Categoría', fontsize=14)
plt.ylabel('Cantidad vendida', fontsize=14)
plt.title('Top categorías más vendidas por tienda', fontsize=16)
plt.xticks(indice, categorias)  # Poner las categorías en el eje X
plt.legend(title='Tienda')

# Mostrar valores arriba de cada barra
for i in range(n_categorias):
    plt.text(indice[i] - 1.5*ancho, tienda1Top[i] + 1, str(int(tienda1Top[i])), ha='center', fontsize=9)
    plt.text(indice[i] - 0.5*ancho, tienda2Top[i] + 1, str(int(tienda2Top[i])), ha='center', fontsize=9)
    plt.text(indice[i] + 0.5*ancho, tienda3Top[i] + 1, str(int(tienda3Top[i])), ha='center', fontsize=9)
    plt.text(indice[i] + 1.5*ancho, tienda4Top[i] + 1, str(int(tienda4Top[i])), ha='center', fontsize=9)

# Ajustar diseño
plt.tight_layout()
plt.show()


# Grafica de ventas por categoria segun el valor monetario
# Datos de cantidad
categorias = top.index.tolist()
tienda1Top = top['Tienda 1'].tolist()
tienda2Top = top['Tienda 2'].tolist()
tienda3Top = top['Tienda 3'].tolist()
tienda4Top = top['Tienda 4'].tolist()

# Datos de valor
valor1Top = valores_top_categorias['Tienda 1'].tolist()
valor2Top = valores_top_categorias['Tienda 2'].tolist()
valor3Top = valores_top_categorias['Tienda 3'].tolist()
valor4Top = valores_top_categorias['Tienda 4'].tolist()

n_categorias = len(categorias)
indice = np.arange(n_categorias)
ancho = 0.2

plt.figure(figsize=(14,7))
plt.bar(indice - 1.5*ancho, valor1Top, width=ancho, label='Tienda 1')
plt.bar(indice - 0.5*ancho, valor2Top, width=ancho, label='Tienda 2')
plt.bar(indice + 0.5*ancho, valor3Top, width=ancho, label='Tienda 3')
plt.bar(indice + 1.5*ancho, valor4Top, width=ancho, label='Tienda 4')
plt.ylabel('Valor vendido ($)', fontsize=12)
plt.title('Top categorías - Valor monetario vendido', fontsize=14)
plt.xticks(indice, categorias)
plt.legend()
plt.show()
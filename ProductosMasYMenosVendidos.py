import pandas as pd
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

tienda1.head()

# Contar el numero por producto
conteoProductosT1 = tienda1['Producto'].value_counts()
conteoProductosT2 = tienda2['Producto'].value_counts()
conteoProductosT3 = tienda3['Producto'].value_counts()
conteoProductosT4 = tienda4['Producto'].value_counts()
# Lista de conteos y nombres de tiendas
conteos = [conteoProductosT1, conteoProductosT2, conteoProductosT3, conteoProductosT4]
tiendas = ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4']

# Para almacenar los datos
topVentas = []

# Recorrer cada tienda
for tienda, conteo in zip(tiendas, conteos):
    # Top 3 más vendidos
    topMas = conteo.nlargest(3)
    # Top 3 menos vendidos
    topMenos = conteo.nsmallest(3)
    for producto, ventas in topMas.items():
        topVentas.append({'Tienda': tienda, 'Producto': producto, 'Ventas': ventas})
    for producto, ventas in topMenos.items():
        topVentas.append({'Tienda': tienda, 'Producto': producto, 'Ventas': ventas})

# Crear los DataFrames
dfTopVentas = pd.DataFrame(topVentas)
dfTopVentas = dfTopVentas.sort_values(by=['Tienda', 'Ventas'], ascending=[True,False])
dfTopVentas.reset_index(drop=True, inplace=True)

# Mostrar resultados
print("Top 3 productos más vendidos por tienda:")
print(dfTopVentas)

# Agrupar por tienda
tiendas_unicas = dfTopVentas['Tienda'].unique()

for tienda in tiendas_unicas:
    df_tienda = dfTopVentas[dfTopVentas['Tienda'] == tienda].reset_index(drop=True)
    
    # Separar más y menos vendidos (primeros 3 son más vendidos)
    df_mas = df_tienda.iloc[:3]
    df_menos = df_tienda.iloc[3:]

    categorias_mas = df_mas['Producto']
    ventas_mas = df_mas['Ventas']

    categorias_menos = df_menos['Producto']
    ventas_menos = df_menos['Ventas']

    # Crear figura con 2 subgráficas
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle(f'{tienda} - Productos más y menos vendidos', fontsize=16)

    # Definir límites comunes para el eje Y
    limite_y = 68

    # Más vendidos
    axs[0].bar(categorias_mas, ventas_mas, color='skyblue', edgecolor='black')
    axs[0].set_title('Más vendidos')
    axs[0].set_ylabel('Cantidad vendida')
    axs[0].set_ylim(0, limite_y)
    axs[0].tick_params(axis='x', rotation=45)  # Rotar etiquetas sin advertencia
    for i, v in enumerate(ventas_mas):
        axs[0].text(i, v + 1, str(v), ha='center', fontsize=9)

    # Menos vendidos
    axs[1].bar(categorias_menos, ventas_menos, color='Coral', edgecolor='black')
    axs[1].set_title('Menos vendidos')
    axs[1].set_ylabel('Cantidad vendida')
    axs[1].set_ylim(0, limite_y)
    axs[1].tick_params(axis='x', rotation=45)
    for i, v in enumerate(ventas_menos):
        axs[1].text(i, v + 1, str(v), ha='center', fontsize=9)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

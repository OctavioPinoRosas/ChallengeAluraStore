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

# Calcular el promedio de calificación por tienda
calificacionTienda1 = tienda1["Calificación"].mean()
calificacionTienda2 = tienda2["Calificación"].mean()
calificacionTienda3 = tienda3["Calificación"].mean()
calificacionTienda4 = tienda4["Calificación"].mean()
# Crear un DataFrame con las calificaciones promedio
calificacionTiendas = pd.DataFrame({
    "Tienda": ["Tienda 1", "Tienda 2", "Tienda 3", "Tienda 4"],
    "Calificacion Promedio": [calificacionTienda1, calificacionTienda2, calificacionTienda3, calificacionTienda4]
})
# Establecer el formato de visualización para los decimales
pd.set_option('display.float_format', '{:,.2f}'.format)
# Mostrar las calificaciones promedio
print(calificacionTiendas)

# Calificacion promedio de cada tienda por año
calificacionTienda1Ano = tienda1.groupby(tienda1['Fecha de Compra'].dt.year)['Calificación'].mean()
calificacionTienda2Ano = tienda2.groupby(tienda2['Fecha de Compra'].dt.year)['Calificación'].mean()
calificacionTienda3Ano = tienda3.groupby(tienda3['Fecha de Compra'].dt.year)['Calificación'].mean()
calificacionTienda4Ano = tienda4.groupby(tienda4['Fecha de Compra'].dt.year)['Calificación'].mean()
calificacionAno = pd.DataFrame({
    'Tienda 1': calificacionTienda1Ano,
    'Tienda 2': calificacionTienda2Ano,
    'Tienda 3': calificacionTienda3Ano,
    'Tienda 4': calificacionTienda4Ano
})
print(calificacionAno)

# Grafica de calificación promedio por tienda
colores = ['purple', 'blue', 'green', 'red'] # Colores parea cada barra
calificacionPromedio = calificacionTiendas["Calificacion Promedio"]
plt.bar(calificacionTiendas["Tienda"],calificacionTiendas["Calificacion Promedio"], color = colores) # Creación de la grafica de barras y sele da un color distinto a cada barra
plt.xlabel('Tiendas')  # Etiquetamos el eje x
plt.ylabel('Calificación')  # Etiquetamos el eje y
plt.title('Calificación promedio por tienda')  # Añadimos un título al gráfico

# Mostrar valores sobre cada barra
for i, valor in enumerate(calificacionPromedio):
    plt.text(i, valor + valor*0.01, f'{valor:,.2f}', ha='center', fontsize=10)

plt.tight_layout()
plt.show()

# Grafica de calificación promedio de cada tienda por año
anos = calificacionAno.index.tolist()
tienda1calificacion = calificacionAno['Tienda 1'].tolist()
tienda2calificacion = calificacionAno['Tienda 2'].tolist()
tienda3calificacion = calificacionAno['Tienda 3'].tolist()
tienda4calificacion = calificacionAno['Tienda 4'].tolist()
# Crear la gráfica
plt.figure(figsize=(12, 6))
plt.ylim(0, 4.5)
# Dibujar líneas para cada tienda
plt.plot(anos, tienda1calificacion, marker='o', label='Tienda 1')
plt.plot(anos, tienda2calificacion, marker='o', label='Tienda 2')
plt.plot(anos, tienda3calificacion, marker='o', label='Tienda 3')
plt.plot(anos, tienda4calificacion, marker='o', label='Tienda 4')
# Configurar etiquetas
plt.xlabel('Años', fontsize=14)
plt.ylabel('Calificación', fontsize=14)
plt.title('Calificación de cada tienda por año', fontsize=16)
plt.legend(title='Tienda')
# Ajustar diseño
plt.xticks(ticks=anos)
plt.tight_layout()
plt.show()
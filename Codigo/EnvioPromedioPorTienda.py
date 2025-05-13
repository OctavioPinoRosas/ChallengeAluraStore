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

# Grafica
envioTienda1 = tienda1["Costo de envío"].mean()
envioTienda2 = tienda2["Costo de envío"].mean()
envioTienda3 = tienda3["Costo de envío"].mean()
envioTienda4 = tienda4["Costo de envío"].mean()

# Crear un DataFrame con las calificaciones promedio
envioTiendas = pd.DataFrame({
    "Tienda": ["Tienda 1", "Tienda 2", "Tienda 3", "Tienda 4"],
    "Costo de envio promedio": [envioTienda1, envioTienda2, envioTienda3, envioTienda4]
})

# Mostrar el DataFrame con las calificaciones promedio
print(envioTiendas)

colores = ['purple', 'blue', 'green', 'red'] # Colores parea cada barra
plt.bar(envioTiendas["Tienda"],envioTiendas["Costo de envio promedio"], color = colores) # Creación de la grafica de barras y sele da un color distinto a cada barra
plt.xlabel('Tiendas')  # Etiquetamos el eje x
plt.ylabel('Costo')  # Etiquetamos el eje y
plt.title('Costo de envio promedio por tienda')  # Añadimos un título al gráfico
for i, valor in enumerate(envioTiendas["Costo de envio promedio"]):
    plt.text(i, valor + 0.5, f'{valor:.2f}', ha='center', va='bottom')
plt.show()
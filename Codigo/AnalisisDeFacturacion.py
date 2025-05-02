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

# Convertir "Fecha de Compra" a tipo fecha
tienda1['Fecha de Compra'] = pd.to_datetime(tienda1['Fecha de Compra'], format='%d/%m/%Y')
tienda2['Fecha de Compra'] = pd.to_datetime(tienda2['Fecha de Compra'], format='%d/%m/%Y')
tienda3['Fecha de Compra'] = pd.to_datetime(tienda3['Fecha de Compra'], format='%d/%m/%Y')
tienda4['Fecha de Compra'] = pd.to_datetime(tienda4['Fecha de Compra'], format='%d/%m/%Y')

# Ingreso total por tienda
ingresoTienda1 = tienda1["Precio"].sum()
ingresoTienda2 = tienda2["Precio"].sum()
ingresoTienda3 = tienda3["Precio"].sum()
ingresoTienda4 = tienda4["Precio"].sum()
ingresoTiendas = pd.DataFrame({
    "Tienda": ["Tienda 1", "Tienda 2", "Tienda 3", "Tienda 4"],
    "Ingreso total": [ingresoTienda1, ingresoTienda2, ingresoTienda3, ingresoTienda4]
})
pd.set_option('display.float_format', '{:,.0f}'.format)
print(ingresoTiendas)

# Ingreso de tiendas por año
ingresosTienda1Ano = tienda1.groupby(tienda1['Fecha de Compra'].dt.year)['Precio'].sum()
ingresosTienda2Ano = tienda2.groupby(tienda2['Fecha de Compra'].dt.year)['Precio'].sum()
ingresosTienda3Ano = tienda3.groupby(tienda3['Fecha de Compra'].dt.year)['Precio'].sum()
ingresosTienda4Ano = tienda4.groupby(tienda4['Fecha de Compra'].dt.year)['Precio'].sum()
ingresosAno = pd.DataFrame({
    'Tienda 1': ingresosTienda1Ano,
    'Tienda 2': ingresosTienda2Ano,
    'Tienda 3': ingresosTienda3Ano,
    'Tienda 4': ingresosTienda4Ano
})
print(ingresosAno)

# Grafica de barras sobre el ingreso total por tienda
colores = ['purple', 'blue', 'green', 'red']
tiendas = ingresoTiendas["Tienda"]
ingresos = ingresoTiendas["Ingreso total"]
plt.figure(figsize=(8, 5))
plt.bar(tiendas, ingresos, color=colores)
plt.xlabel('Tiendas')
plt.ylabel('Ingresos totales')
plt.title('Ingreso total por tienda')
# Mostrar valores arriba de cada barra
for i, valor in enumerate(ingresos):
    plt.text(i, valor + valor*0.01, f'{valor:,.0f}', ha='center', fontsize=10)

plt.tight_layout()
plt.show()


# Grafica sobre el ingreso total por año de cada tienda
anos = ingresosAno.index.tolist()
tienda1ingresos = ingresosAno['Tienda 1'].tolist()
tienda2ingresos = ingresosAno['Tienda 2'].tolist()
tienda3ingresos = ingresosAno['Tienda 3'].tolist()
tienda4ingresos = ingresosAno['Tienda 4'].tolist()
# Crear la gráfica
plt.figure(figsize=(12, 6))
# Dibujar líneas para cada tienda
plt.plot(anos, tienda1ingresos, marker='o', label='Tienda 1')
plt.plot(anos, tienda2ingresos, marker='o', label='Tienda 2')
plt.plot(anos, tienda3ingresos, marker='o', label='Tienda 3')
plt.plot(anos, tienda4ingresos, marker='o', label='Tienda 4')
# Configurar etiquetas
plt.xlabel('Años', fontsize=14)
plt.ylabel('Ingresos', fontsize=14)
plt.title('Ingresos de cada tienda por año', fontsize=16)
plt.legend(title='Tienda')
# Ajustar diseño
plt.xticks(ticks=anos)
plt.tight_layout()
plt.show()
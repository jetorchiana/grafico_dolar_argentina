import pandas as pd
import matplotlib.pyplot as plt

# leer archivo CSV
df = pd.read_csv("dolar_argentina.csv")

# crear grafico de linea
plt.plot(df ["mes"], df["tipo_cambio"], marker = 'o')
plt.title("evolucion del dolar en argentina")
plt.xlabel("mes") 
plt.ylabel("precio en pesos")
plt.grid(True)

#guardar y mostrar
plt.savefig("grafico_dolar.png")
plt.show()


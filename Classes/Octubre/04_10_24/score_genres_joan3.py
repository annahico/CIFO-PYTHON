import time

import pandas as pd

inicial = time.time()
# Carreguem el CSV a un DataFrame
df = pd.read_csv("C:\\Users\\Usuario\\Desktop\\Marvel_DC.csv",
                 encoding='utf-8')

# Substituïm les cel·les buides o amb dobles cometes
df.replace({"": None, '""': None, ',,': ',ND,'}, regex=True, inplace=True)

# Assegurem que la columna de puntuació és un float (assumint que la columna 6 és el "score")
df['score'] = df.iloc[:, 6].astype(float)

# Agrupem per la columna de gènere (assumint que la columna 3 és el "gènere")
grouped = df.groupby(df.columns[3])['score'].mean()

# Mostrem els resultats
for genere, puntuacio_mitjana in grouped.items():
    print(f"{genere}: {puntuacio_mitjana}")
final = time.time()
print(final-inicial)

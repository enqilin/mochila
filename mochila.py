import pandas as pd

df = pd.read_csv('pokemon.csv')
df['capture_rate'] = df['capture_rate'].drop(df[df['capture_rate'] == '30 (Meteorite)255 (Core)'].index)
df['capture_rate'].fillna(0, inplace=True)
df['capture_rate'] = df['capture_rate'].astype(int)
df['peso'] = 1 - df['capture_rate'] / df['capture_rate'].max()
df['beneficio'] = (df['base_total'] / df['base_total'].max())
df.drop_duplicates(subset = ['abilities'] or ['type_1'] and['type_2'], keep = 'last', inplace = True)
columns_1 = ['name','beneficio','peso']
df_3=df[columns_1]
df_3.fillna(0, inplace=True)
df_3.to_csv('../mochila/pokemon_no_normalizar.csv', index=False)
a = df_3['peso'] > 0
df_3 = df_3[a]
df_4 = df_3
df_4.to_csv('../mochila/pokemon_normalizar.csv', index=False)


def es_solucion(solucion, capacidad):
    total = 0
    for i in solucion:
        total = round(total + i[2],2)
        return total < capacidad
    if total == capacidad:
        return True
    else:
        return False
    

def mochila_pokemon(conjunto_candidatos,capacidad,peso):
    solucion = []
    restante = peso
    while  capacidad!=0 and es_solucion(conjunto_candidatos, capacidad):
        dato = conjunto_candidatos.pop()
        if dato[2] <= restante:
            solucion.append(dato)
            restante = round(restante - dato[2]*10,2)
    return solucion , peso
objectos = df_4.values.tolist()
port_term =[]
cap_max = 6
peso_max = 10
for i in objectos:
    i.append(i[2]/(i[1]))
objectos.sort(key=lambda x: x[3], reverse=True)
port_term = mochila_pokemon(objectos, cap_max,peso_max)
print("La mochila tiene una capacidad de: ", cap_max)
print(port_term)
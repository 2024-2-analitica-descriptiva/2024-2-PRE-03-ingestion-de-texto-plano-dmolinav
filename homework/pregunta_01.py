
import pandas as pd

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.
    """
    with open('files/input/clusters_report.txt', 'r', encoding='utf-8') as archivo:
        todas_las_lineas = archivo.readlines()

    with open('files/input/clusters_report.txt', 'r', encoding='utf-8') as archivo:
        lineas_archivo = archivo.readlines()

    lineas_datos = lineas_archivo[4:]

    tabla_datos = [["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"]]

    fila_temporal = []
    es_primera_linea = True

    for linea_actual in lineas_datos:
        linea_actual = linea_actual.strip()
        linea_dividida = linea_actual.split()
        if len(linea_dividida) > 0 and es_primera_linea:
            fila_temporal.append(int(linea_dividida[0]))  # nmmero del cluster
            fila_temporal.append(int(linea_dividida[1]))  # Cantidad de palabras clave
            fila_temporal.append(float(linea_dividida[2].replace(',', '.')))  # Porcentaje de palabras clave
            fila_temporal.append(" ".join(linea_dividida[4:]))  # Principales palabras clave
            es_primera_linea = False

        elif len(linea_dividida) > 0:
            fila_temporal.append(" ".join(linea_dividida))

        else:
          es_primera_linea = True
          fila_temporal[3] = ' '.join(fila_temporal[3:]).replace('.', '')  # Unir las palabras clave
          tabla_datos.append(fila_temporal[:4])  # Agregar fila 
          fila_temporal = []  # Reiniciar fila 

    return(pd.DataFrame(tabla_datos[1:], columns=tabla_datos[0]))

print(pregunta_01())

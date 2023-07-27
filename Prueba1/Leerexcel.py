import openpyxl
import pandas as pd

def leer_documento_csv(nombre_archivo):
    try:
        df = pd.read_csv(nombre_archivo, sep=";", header=None)
        return df
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
        return pd.DataFrame()  # Devuelve un DataFrame vacío en caso de error
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return pd.DataFrame()  # Devuelve un DataFrame vacío en caso de error

def analizar_datos(df):
    if not df.empty:
        estadisticas = df.describe()
        print(estadisticas)
    else:
        print("No se pudieron leer los datos del archivo CSV.")

def guardar_en_excel(df, nombre_archivo_excel):
    try:
        df.to_excel(nombre_archivo_excel, index=False, header=False)
        print(f"Los datos se han guardado en '{nombre_archivo_excel}' correctamente.")
    except Exception as e:
        print(f"Ocurrió un error al guardar los datos en Excel: {e}")

def eliminar_datos_excel(nombre_archivo_excel):
    try:
        libro_excel = openpyxl.load_workbook(nombre_archivo_excel)# Abre el archivo Excel        
        hoja = libro_excel.active # Selecciona la primera hoja (puedes ajustar esto si necesitas otra hoja)
        hoja.delete_rows(1, hoja.max_row) # Elimina los datos de todas las filas

        # Guarda los cambios
        libro_excel.save(nombre_archivo_excel)
        libro_excel.close()

        print(f"Se han eliminado todos los datos de '{nombre_archivo_excel}' correctamente.")
    except Exception as e:
        print(f"Ocurrió un error al eliminar los datos: {e}")

# Ejemplo de uso:
#nombre_archivo_csv = "Prueba de capacidades técnicas - Listado de participantes - reto No. 1 (1).csv"  # Reemplaza con la ruta real de tu archivo CSV

# Leer el archivo CSV
#df_datos = leer_documento_csv(nombre_archivo_csv)

# Analizar los datos
#analizar_datos(df_datos)

# Eliminar los datos del archivo Excel
#eliminar_datos_excel(nombre_archivo_excel)
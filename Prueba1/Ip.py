
import xlsxwriter
import openpyxl
import requests
import Leerexcel
import Exc
import pandas as pd

libro = xlsxwriter.Workbook('IP_Direccion.xlsx')
hoja = libro.add_worksheet("FirstSheet")

def analizar_columnas(data):
    if not data.empty:
        participante = data.iloc[:, 0]  # Selecciona la primera columna del DataFrame
        ip = data.iloc[:, 1]  # Selecciona la segunda columna del DataFrame
        #print(f"Participante: {participante}, Ip: {ip}")
        # Realizar el análisis de la segunda columna aquí
        #estadisticas_ip = ip.describe()# Por ejemplo, obtener estadísticas descriptivas de la columna
        #data_sep = [participante, ip]
        #print(estadisticas_ip)
        #datas = [participante,ip]
        #obtener_pais_por_ip(participante,ip)
        
    else:
        print("No se pudieron leer los datos del archivo CSV.")
def recorrer_arreglo(arreglo):
    fila = 1
    datos_a_guardar = []  # Lista para almacenar los datos procesados
    #while fila < len(arreglo): #Aqui podemos usar todas las de la lista
    while fila < 50:        #Solo usare 50
        a = arreglo.iloc[fila][0]
        b = arreglo.iloc[fila][1]
        data = obtener_pais_por_ip(a, b)
        if data is not None:  # Verificar que se obtuvieron datos válidos
            datos_a_guardar.append(data)  # Agregar los datos a la lista

        fila += 1
    #No se pudo obtener información para la dirección IP 201.218.207.82. Error: HTTPConnectionPool(host='ip-api.com', port=80): Read timed out. (read timeout=None)
    #avece el api recibe tantas request que no las puede procesar por eso utilizo un numero bajo como demostracion
    # Convertir la lista de datos a un DataFrame
    df_datos_a_guardar = pd.DataFrame(datos_a_guardar)
    # Guardar los datos procesados en el archivo Excel
    Leerexcel.guardar_en_excel(df_datos_a_guardar, "IP_Direccion.xlsx")

def obtener_pais_por_ip(participante, ip):
    
    if ip is None:
        print(f"Participante {participante} no tiene dirección IP.")
        return
    url = f"http://ip-api.com/json/{ip}" #despues de 40 datos ocurre un error con el api
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()
        if datos["status"] == "success":
            pais = datos["country"]
            dato_para_excel = {'Participante': participante, 'Pais': pais, 'Ip': ip}
            print(f"Participante {participante}: La dirección IP {ip} está ubicada en {pais}.")          
        else:
            print(f"No se pudo obtener información para la dirección IP {ip}.")     
        #return dato_para_excel 
    except requests.exceptions.RequestException as e:
        # Si ocurre un error en la solicitud, imprimir un mensaje y retornar None
        print(f"No se pudo obtener información para la dirección IP {ip}. Error: {e}")
        return None
    return dato_para_excel
def main():
    nombre_archivo_csv = "Prueba de capacidades técnicas - Listado de participantes - reto No. 1 (1).csv"  # Reemplaza con la ruta real de tu archivo CSV
    nombre_archivo_excel = "IP_Direccion.xlsx"
    Leerexcel.eliminar_datos_excel(nombre_archivo_excel)#Para que no se acumulen los datos primero los borro, puedo solo editarlos pero prefiero borrarlos antes de empezar
    print(f"hola")
    df_datos = Leerexcel.leer_documento_csv(nombre_archivo_csv)
    print(df_datos)
    #analizar_columnas(df_datos)
    #Leerexcel.guardar_en_excel(df_datos, "IP_Direccion.xlsx")
    recorrer_arreglo(df_datos)
    return 0

if __name__ == "__main__":
    main()
    
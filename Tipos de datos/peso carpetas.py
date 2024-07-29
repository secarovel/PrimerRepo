import os

def obtener_peso_carpeta(ruta):
    total_peso = 0
    for dirpath, dirnames, filenames in os.walk(ruta):
        for filename in filenames:
            archivo_ruta = os.path.join(dirpath, filename)
            total_peso += os.path.getsize(archivo_ruta)
    return total_peso

def obtener_pesos_subcarpetas(ruta):
    pesos_subcarpetas = {}
    for dirpath, dirnames, filenames in os.walk(ruta):
        peso_carpeta = obtener_peso_carpeta(dirpath)
        pesos_subcarpetas[dirpath] = peso_carpeta
    return pesos_subcarpetas

def main():
    ruta_directorio = input("Introduce la ruta del directorio: ")
    try:
        pesos_subcarpetas = obtener_pesos_subcarpetas(ruta_directorio)
        for carpeta, peso in pesos_subcarpetas.items():
            print(f"El peso de la carpeta '{carpeta}' es: {peso} bytes")
    except FileNotFoundError:
        print("El directorio no fue encontrado.")
    except PermissionError:
        print("No tienes permisos para acceder al directorio.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
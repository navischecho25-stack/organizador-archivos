import os
import shutil

def crear_archivos_prueba():
    """Crea archivos de diferentes tipos para probar el organizador."""
    print("🛠️ Creando archivos de prueba desordenados...")
    
    archivos_prueba = {
        "reporte_ventas.csv": "datos,ventas,100",
        "manual_usuario.pdf": "%PDF-1.3 contenido de prueba",
        "notas_reunion.txt": "Recordatorios importantes del proyecto",
        "datos_clientes.csv": "id,nombre,correo",
        "factura.pdf": "%PDF-1.3 factura corporativa"
    }
    
    for nombre, contenido in archivos_prueba.items():
        if not os.path.exists(nombre):
            with open(nombre, "w", encoding="utf-8") as f:
                f.write(contenido)
                
    print("✅ Archivos de prueba creados con éxito en la carpeta.")

def organizar_archivos():
    # Asegurarnos de tener archivos para organizar
    crear_archivos_prueba()
    
    print("\n📁 Iniciando organización automática de archivos...")
    
    # Definir las carpetas de destino según la extensión
    extensiones_carpetas = {
        ".pdf": "Carpeta_PDFs",
        ".csv": "Carpeta_CSVs",
        ".txt": "Carpeta_Textos"
    }
    
    # Crear las carpetas de destino si no existen
    for carpeta in extensiones_carpetas.values():
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
            print(f"📂 Carpeta creada: {carpeta}/")
            
    # Obtener todos los archivos del directorio actual
    archivos = os.listdir(".")
    
    movidos = 0
    for archivo in archivos:
        # Ignorar directorios y el propio script
        if os.path.isdir(archivo) or archivo == "organizador_archivos.py":
            continue
            
        # Obtener la extensión del archivo
        _, extension = os.path.splitext(archivo)
        
        # Si la extensión está en nuestro diccionario, mover el archivo
        if extension in extensiones_carpetas:
            carpeta_destino = extensiones_carpetas[extension]
            origen = archivo
            destino = os.path.join(carpeta_destino, archivo)
            
            shutil.move(origen, destino)
            print(f"🚚 Movido: '{archivo}' ➡️  '{carpeta_destino}/'")
            movidos += 1
            
    print("\n" + "="*40)
    print("✨ ¡ORGANIZACIÓN COMPLETADA CON ÉXITO!")
    print(f"📊 Total de archivos organizados: {movidos}")
    print("="*40)

if __name__ == "__main__":
    organizar_archivos()
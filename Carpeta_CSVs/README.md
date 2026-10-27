# 📂 Organizador Automático de Archivos (`organizador_archivos.py`)

## 🎯 Descripción del Proyecto
Este script de automatización en Python (BPA - Business Process Automation) soluciona un problema común de gestión de archivos: el desorden en directorios de trabajo. El programa analiza los archivos sueltos, identifica sus extensiones y los clasifica automáticamente en subcarpetas ordenadas de manera limpia y eficiente.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.14
* **Módulos Nativos:** `os` (gestión de directorios y rutas) y `shutil` (operaciones de movimiento de archivos de alto nivel).

## 🚀 Características
* **Generación de Pruebas Autónomas:** Crea un set de archivos de prueba variados (`.csv`, `.pdf`, `.txt`) al ejecutarse por primera vez si el directorio está vacío.
* **Clasificación Dinámica:** Agrupa los documentos según su extensión de forma automatizada (`Carpeta_PDFs`, `Carpeta_CSVs`, `Carpeta_Textos`).
* **Prevención de Errores:** Filtra directorios y omite el propio script para garantizar una ejecución segura.

## 💻 Instrucciones de Uso
1. Coloca los archivos que deseas organizar en la carpeta del proyecto.
2. Ejecuta el script:
   ```bash
   python organizador_archivos.py
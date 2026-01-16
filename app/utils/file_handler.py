"""
Módulo para gestión de archivos.
Reutilizable para todas las herramientas futuras.
"""
import os
import time
import zipfile
from pathlib import Path
from flask import current_app

def save_uploaded_file(file, folder):
    """
    Guarda un archivo subido en la carpeta especificada.
    
    Args:
        file: Archivo de Flask request.files
        folder: Carpeta donde guardar el archivo
        
    Returns:
        str: Ruta completa del archivo guardado
    """
    # Generar nombre único basado en timestamp
    timestamp = int(time.time() * 1000)
    filename = f"{timestamp}_{file.filename}"
    filepath = os.path.join(folder, filename)
    
    file.save(filepath)
    return filepath

def create_zip_from_files(file_paths, output_path):
    """
    Crea un archivo ZIP con los archivos especificados.
    
    Args:
        file_paths: Lista de rutas de archivos a incluir
        output_path: Ruta donde guardar el ZIP
        
    Returns:
        str: Ruta del archivo ZIP creado
    """
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in file_paths:
            if os.path.exists(file_path):
                # Usar solo el nombre del archivo en el ZIP
                zipf.write(file_path, os.path.basename(file_path))
    return output_path

def cleanup_old_files(folder, max_age_minutes=None):
    """
    Elimina archivos antiguos de una carpeta.
    
    Args:
        folder: Carpeta a limpiar
        max_age_minutes: Edad máxima en minutos (None usa la configuración de la app)
    """
    if max_age_minutes is None:
        max_age_minutes = current_app.config.get('CLEANUP_AFTER_MINUTES', 10)
    
    current_time = time.time()
    max_age_seconds = max_age_minutes * 60
    
    if not os.path.exists(folder):
        return
    
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        try:
            if os.path.isfile(filepath):
                file_age = current_time - os.path.getmtime(filepath)
                if file_age > max_age_seconds:
                    os.remove(filepath)
        except Exception as e:
            # Log error pero continuar con otros archivos
            print(f"Error eliminando {filepath}: {e}")

def delete_file(filepath):
    """Elimina un archivo específico."""
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
            return True
    except Exception as e:
        print(f"Error eliminando {filepath}: {e}")
    return False

def get_file_size_mb(filepath):
    """Obtiene el tamaño de un archivo en MB."""
    if os.path.exists(filepath):
        return os.path.getsize(filepath) / (1024 * 1024)
    return 0

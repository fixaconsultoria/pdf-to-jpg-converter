"""
Módulo de conversión de archivos.
Contiene la lógica de conversión reutilizable.
Para nuevas herramientas, agregar nuevas funciones aquí o crear módulos específicos.
"""
import os
from pdf2image import convert_from_path
from PIL import Image
import tempfile

def pdf_to_jpg(pdf_path, output_folder, dpi=200):
    """
    Convierte un PDF a imágenes JPG.
    Cada página se convierte en una imagen separada.
    
    Args:
        pdf_path: Ruta del archivo PDF
        output_folder: Carpeta donde guardar las imágenes
        dpi: Resolución de las imágenes (default: 200)
        
    Returns:
        list: Lista de rutas de las imágenes JPG creadas
    """
    jpg_files = []
    
    try:
        # Convertir PDF a imágenes
        # poppler_path puede ser necesario en algunos sistemas
        images = convert_from_path(
            pdf_path,
            dpi=dpi,
            output_folder=None,
            fmt='jpeg'
        )
        
        # Guardar cada página como JPG
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        
        for i, image in enumerate(images, start=1):
            jpg_filename = f"{base_name}_page_{i}.jpg"
            jpg_path = os.path.join(output_folder, jpg_filename)
            
            # Convertir a RGB si es necesario (algunos PDFs pueden tener modo diferente)
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Guardar como JPG con calidad 95
            image.save(jpg_path, 'JPEG', quality=95)
            jpg_files.append(jpg_path)
        
        return jpg_files
    
    except Exception as e:
        # Limpiar archivos creados en caso de error
        for jpg_file in jpg_files:
            try:
                if os.path.exists(jpg_file):
                    os.remove(jpg_file)
            except:
                pass
        raise Exception(f"Error al convertir PDF a JPG: {str(e)}")

# Ejemplo de cómo agregar nuevas funciones de conversión en el futuro:
# def pdf_to_png(pdf_path, output_folder, dpi=200):
#     """Convierte PDF a PNG."""
#     pass
#
# def jpg_to_pdf(jpg_paths, output_path):
#     """Convierte múltiples JPG a un PDF."""
#     pass
#
# def compress_pdf(pdf_path, output_path, quality='medium'):
#     """Comprime un PDF."""
#     pass

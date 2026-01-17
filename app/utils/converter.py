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

def pdf_to_png(pdf_path, output_folder, dpi=200):
    """
    Convierte un PDF a imágenes PNG.
    Cada página se convierte en una imagen separada.
    
    Args:
        pdf_path: Ruta del archivo PDF
        output_folder: Carpeta donde guardar las imágenes
        dpi: Resolución de las imágenes (default: 200)
        
    Returns:
        list: Lista de rutas de las imágenes PNG creadas
    """
    png_files = []
    
    try:
        # Convertir PDF a imágenes
        images = convert_from_path(
            pdf_path,
            dpi=dpi,
            output_folder=None,
            fmt='png'
        )
        
        # Guardar cada página como PNG
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        
        for i, image in enumerate(images, start=1):
            png_filename = f"{base_name}_page_{i}.png"
            png_path = os.path.join(output_folder, png_filename)
            
            # Guardar como PNG
            image.save(png_path, 'PNG')
            png_files.append(png_path)
        
        return png_files
    
    except Exception as e:
        # Limpiar archivos creados en caso de error
        for png_file in png_files:
            try:
                if os.path.exists(png_file):
                    os.remove(png_file)
            except:
                pass
        raise Exception(f"Error al convertir PDF a PNG: {str(e)}")

def jpg_to_pdf(jpg_paths, output_path):
    """
    Convierte múltiples imágenes JPG a un PDF.
    
    Args:
        jpg_paths: Lista de rutas de archivos JPG
        output_path: Ruta donde guardar el PDF
        
    Returns:
        str: Ruta del PDF creado
    """
    try:
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.utils import ImageReader
        
        # Si reportlab no está disponible, usar Pillow
        try:
            images = []
            for jpg_path in sorted(jpg_paths):
                if os.path.exists(jpg_path):
                    img = Image.open(jpg_path)
                    # Convertir a RGB si es necesario
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    images.append(img)
            
            if not images:
                raise Exception("No se encontraron imágenes válidas")
            
            # Guardar como PDF usando Pillow
            if images:
                images[0].save(
                    output_path,
                    'PDF',
                    resolution=100.0,
                    save_all=True,
                    append_images=images[1:] if len(images) > 1 else []
                )
            
            return output_path
            
        except ImportError:
            raise Exception("Error: No se puede crear PDF. Se requiere Pillow.")
    
    except Exception as e:
        # Eliminar PDF si se creó parcialmente
        try:
            if os.path.exists(output_path):
                os.remove(output_path)
        except:
            pass
        raise Exception(f"Error al convertir JPG a PDF: {str(e)}")

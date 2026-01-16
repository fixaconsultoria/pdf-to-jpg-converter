"""
Endpoint para la herramienta PDF a JPG.
Este es un ejemplo de cómo estructurar nuevas herramientas.
Para agregar una nueva herramienta, crear un archivo similar con su propia lógica.
"""
from flask import Blueprint, request, jsonify, send_file, current_app
import os
import time
from app.utils.file_handler import (
    save_uploaded_file,
    create_zip_from_files,
    cleanup_old_files,
    delete_file
)
from app.utils.converter import pdf_to_jpg

# Crear blueprint para esta herramienta
# El nombre del blueprint puede ser usado para URLs: /pdf-to-jpg/...
bp = Blueprint('pdf_to_jpg', __name__, url_prefix='/api/pdf-to-jpg')

@bp.route('/convert', methods=['POST'])
def convert_pdf_to_jpg():
    """
    Endpoint principal para convertir PDF a JPG.
    
    Flujo:
    1. Recibe archivo PDF
    2. Valida el archivo
    3. Convierte a JPG
    4. Crea ZIP con todas las imágenes
    5. Retorna el ZIP para descarga
    """
    try:
        # Validar que se haya enviado un archivo
        if 'file' not in request.files:
            return jsonify({'error': 'No se ha enviado ningún archivo'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No se ha seleccionado ningún archivo'}), 400
        
        # Validar extensión
        if not file.filename.lower().endswith('.pdf'):
            return jsonify({'error': 'El archivo debe ser un PDF'}), 400
        
        # Limpiar archivos antiguos antes de procesar
        cleanup_old_files(current_app.config['UPLOAD_FOLDER'])
        cleanup_old_files(current_app.config['OUTPUT_FOLDER'])
        
        # Guardar archivo subido
        upload_path = save_uploaded_file(
            file,
            current_app.config['UPLOAD_FOLDER']
        )
        
        try:
            # Convertir PDF a JPG
            jpg_files = pdf_to_jpg(
                upload_path,
                current_app.config['OUTPUT_FOLDER']
            )
            
            if not jpg_files:
                return jsonify({'error': 'No se pudieron generar imágenes del PDF'}), 500
            
            # Crear ZIP con todas las imágenes
            timestamp = int(time.time() * 1000)
            zip_filename = f"pdf_images_{timestamp}.zip"
            zip_path = os.path.join(current_app.config['OUTPUT_FOLDER'], zip_filename)
            
            create_zip_from_files(jpg_files, zip_path)
            
            # Limpiar archivos JPG individuales (ya están en el ZIP)
            for jpg_file in jpg_files:
                delete_file(jpg_file)
            
            # Enviar ZIP como respuesta
            return send_file(
                zip_path,
                as_attachment=True,
                download_name=zip_filename,
                mimetype='application/zip'
            )
        
        finally:
            # Eliminar PDF original después de procesar
            delete_file(upload_path)
            # El ZIP se eliminará automáticamente después de unos minutos por cleanup_old_files
    
    except Exception as e:
        return jsonify({'error': f'Error al procesar el archivo: {str(e)}'}), 500

@bp.route('/health', methods=['GET'])
def health_check():
    """Endpoint de salud para verificar que el servicio está funcionando."""
    return jsonify({'status': 'ok', 'tool': 'pdf-to-jpg'})

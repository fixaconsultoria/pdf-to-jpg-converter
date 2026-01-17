"""
Endpoint para la herramienta PDF a PNG.
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
from app.utils.converter import pdf_to_png

bp = Blueprint('pdf_to_png', __name__, url_prefix='/api/pdf-to-png')

@bp.route('/convert', methods=['POST'])
def convert_pdf_to_png():
    """Endpoint principal para convertir PDF a PNG."""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No se ha enviado ningún archivo'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No se ha seleccionado ningún archivo'}), 400
        
        if not file.filename.lower().endswith('.pdf'):
            return jsonify({'error': 'El archivo debe ser un PDF'}), 400
        
        cleanup_old_files(current_app.config['UPLOAD_FOLDER'])
        cleanup_old_files(current_app.config['OUTPUT_FOLDER'])
        
        upload_path = save_uploaded_file(
            file,
            current_app.config['UPLOAD_FOLDER']
        )
        
        try:
            png_files = pdf_to_png(
                upload_path,
                current_app.config['OUTPUT_FOLDER']
            )
            
            if not png_files:
                return jsonify({'error': 'No se pudieron generar imágenes del PDF'}), 500
            
            timestamp = int(time.time() * 1000)
            zip_filename = f"pdf_images_{timestamp}.zip"
            zip_path = os.path.join(current_app.config['OUTPUT_FOLDER'], zip_filename)
            
            create_zip_from_files(png_files, zip_path)
            
            for png_file in png_files:
                delete_file(png_file)
            
            return send_file(
                zip_path,
                as_attachment=True,
                download_name=zip_filename,
                mimetype='application/zip'
            )
        
        finally:
            delete_file(upload_path)
    
    except Exception as e:
        return jsonify({'error': f'Error al procesar el archivo: {str(e)}'}), 500

@bp.route('/health', methods=['GET'])
def health_check():
    """Endpoint de salud."""
    return jsonify({'status': 'ok', 'tool': 'pdf-to-png'})

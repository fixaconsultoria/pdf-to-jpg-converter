"""
Endpoint para la herramienta JPG a PDF.
Permite subir múltiples imágenes JPG y convertirlas en un PDF.
"""
from flask import Blueprint, request, jsonify, send_file, current_app
import os
import time
from app.utils.file_handler import (
    save_uploaded_file,
    cleanup_old_files,
    delete_file
)
from app.utils.converter import jpg_to_pdf

bp = Blueprint('jpg_to_pdf', __name__, url_prefix='/api/jpg-to-pdf')

@bp.route('/convert', methods=['POST'])
def convert_jpg_to_pdf():
    """Endpoint principal para convertir múltiples JPG a PDF."""
    try:
        # Verificar que se hayan enviado archivos
        if 'files' not in request.files:
            return jsonify({'error': 'No se han enviado archivos'}), 400
        
        files = request.files.getlist('files')
        
        if not files or files[0].filename == '':
            return jsonify({'error': 'No se han seleccionado archivos'}), 400
        
        # Validar que sean imágenes JPG/JPEG
        jpg_paths = []
        upload_paths = []
        
        for file in files:
            if file.filename == '':
                continue
            
            filename_lower = file.filename.lower()
            if not (filename_lower.endswith('.jpg') or filename_lower.endswith('.jpeg')):
                # Limpiar archivos ya subidos si hay error
                for path in upload_paths:
                    delete_file(path)
                return jsonify({'error': 'Todos los archivos deben ser JPG/JPEG'}), 400
        
        cleanup_old_files(current_app.config['UPLOAD_FOLDER'])
        cleanup_old_files(current_app.config['OUTPUT_FOLDER'])
        
        # Guardar todos los archivos
        for file in files:
            if file.filename:
                upload_path = save_uploaded_file(
                    file,
                    current_app.config['UPLOAD_FOLDER']
                )
                upload_paths.append(upload_path)
                jpg_paths.append(upload_path)
        
        if not jpg_paths:
            return jsonify({'error': 'No se pudieron guardar los archivos'}), 500
        
        try:
            # Crear PDF
            timestamp = int(time.time() * 1000)
            pdf_filename = f"images_{timestamp}.pdf"
            pdf_path = os.path.join(current_app.config['OUTPUT_FOLDER'], pdf_filename)
            
            jpg_to_pdf(jpg_paths, pdf_path)
            
            if not os.path.exists(pdf_path):
                return jsonify({'error': 'No se pudo crear el PDF'}), 500
            
            # Enviar PDF
            return send_file(
                pdf_path,
                as_attachment=True,
                download_name=pdf_filename,
                mimetype='application/pdf'
            )
        
        finally:
            # Limpiar archivos JPG subidos
            for path in upload_paths:
                delete_file(path)
            # El PDF se eliminará automáticamente después de unos minutos
    
    except Exception as e:
        return jsonify({'error': f'Error al procesar los archivos: {str(e)}'}), 500

@bp.route('/health', methods=['GET'])
def health_check():
    """Endpoint de salud."""
    return jsonify({'status': 'ok', 'tool': 'jpg-to-pdf'})

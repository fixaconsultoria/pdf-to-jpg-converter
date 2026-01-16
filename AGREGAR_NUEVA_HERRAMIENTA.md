# Guía: Cómo Agregar una Nueva Herramienta

Esta guía te muestra paso a paso cómo agregar una nueva herramienta de conversión siguiendo la arquitectura modular del proyecto.

## Ejemplo: Agregar "PDF a PNG"

### Paso 1: Crear función de conversión

Edita `app/utils/converter.py` y agrega:

```python
def pdf_to_png(pdf_path, output_folder, dpi=200):
    """
    Convierte un PDF a imágenes PNG.
    
    Args:
        pdf_path: Ruta del archivo PDF
        output_folder: Carpeta donde guardar las imágenes
        dpi: Resolución de las imágenes (default: 200)
        
    Returns:
        list: Lista de rutas de las imágenes PNG creadas
    """
    png_files = []
    
    try:
        images = convert_from_path(pdf_path, dpi=dpi, fmt='png')
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        
        for i, image in enumerate(images, start=1):
            png_filename = f"{base_name}_page_{i}.png"
            png_path = os.path.join(output_folder, png_filename)
            image.save(png_path, 'PNG')
            png_files.append(png_path)
        
        return png_files
    except Exception as e:
        # Limpiar en caso de error
        for png_file in png_files:
            try:
                if os.path.exists(png_file):
                    os.remove(png_file)
            except:
                pass
        raise Exception(f"Error al convertir PDF a PNG: {str(e)}")
```

### Paso 2: Crear endpoint

Crea `app/routes/pdf_to_png.py`:

```python
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
```

### Paso 3: Registrar el blueprint

Edita `app/__init__.py` y agrega:

```python
from app.routes import pdf_to_png
app.register_blueprint(pdf_to_png.bp)
```

### Paso 4: Crear página HTML (opcional)

Si quieres una página separada, crea `templates/pdf_to_png.html` (similar a `index.html`) y agrega una ruta:

```python
@app.route('/pdf-to-png')
def pdf_to_png_page():
    return render_template('pdf_to_png.html')
```

### Paso 5: Adaptar JavaScript (si es necesario)

Si creaste una página separada, copia `static/js/main.js` a `static/js/pdf_to_png.js` y cambia:

```javascript
const API_ENDPOINT = '/api/pdf-to-png/convert';
```

## Estructura de Archivos Resultante

```
app/
├── routes/
│   ├── pdf_to_jpg.py    (existente)
│   └── pdf_to_png.py    (nuevo)
├── utils/
│   ├── converter.py     (actualizado con nueva función)
│   └── file_handler.py  (sin cambios, reutilizable)
```

## Notas Importantes

1. **Reutilización**: Las funciones en `file_handler.py` son completamente reutilizables. No necesitas modificarlas.

2. **Nomenclatura**: Sigue la convención de nombres:
   - Archivos: `snake_case.py`
   - Blueprints: `snake_case`
   - URLs: `/api/kebab-case`

3. **Validación**: Siempre valida:
   - Tipo de archivo
   - Tamaño (ya está limitado por Flask a 20MB)
   - Existencia del archivo

4. **Limpieza**: Usa `cleanup_old_files()` y `delete_file()` para mantener el servidor limpio.

5. **Errores**: Siempre maneja errores y retorna mensajes claros al usuario.

## Ejemplos de Otras Herramientas Posibles

- **JPG a PDF**: Múltiples imágenes → un PDF
- **Comprimir PDF**: Reducir tamaño de PDF
- **Dividir PDF**: Separar páginas en múltiples PDFs
- **Unir PDFs**: Combinar múltiples PDFs en uno
- **PDF a Word**: Conversión a formato DOCX
- **Rotar PDF**: Rotar páginas del PDF

Cada una seguiría el mismo patrón: función de conversión + endpoint + (opcional) página HTML.

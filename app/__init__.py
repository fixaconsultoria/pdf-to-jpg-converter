"""
Aplicación Flask principal.
Configuración centralizada para facilitar la expansión con nuevas herramientas.
"""
from flask import Flask
import os

def create_app():
    """Factory function para crear la aplicación Flask."""
    # Obtener el directorio base del proyecto (un nivel arriba de app/)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    app = Flask(__name__, 
                template_folder=os.path.join(base_dir, 'templates'),
                static_folder=os.path.join(base_dir, 'static'))
    
    # Configuración de la aplicación
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024  # 20 MB máximo
    app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'uploads')
    app.config['OUTPUT_FOLDER'] = os.path.join(os.path.dirname(__file__), 'outputs')
    app.config['CLEANUP_AFTER_MINUTES'] = 10  # Limpiar archivos después de 10 minutos
    
    # Crear carpetas si no existen
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)
    
    # Ruta principal (página de inicio)
    @app.route('/')
    def index():
        from flask import render_template
        return render_template('index.html')
    
    # Registrar blueprints (rutas)
    # Para agregar nuevas herramientas, crear un nuevo archivo en routes/ y registrarlo aquí
    from app.routes import pdf_to_jpg
    app.register_blueprint(pdf_to_jpg.bp)
    
    # Ejemplo de cómo agregar más herramientas en el futuro:
    # from app.routes import pdf_to_png
    # app.register_blueprint(pdf_to_png.bp)
    # from app.routes import jpg_to_pdf
    # app.register_blueprint(jpg_to_pdf.bp)
    
    return app

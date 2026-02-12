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
    
    # Rutas de páginas principales (URLs SEO-friendly)
    @app.route('/')
    def index():
        from flask import render_template
        return render_template('index.html')
    
    @app.route('/pdf-a-jpg')
    @app.route('/pdf-to-jpg')  # Mantener compatibilidad
    def pdf_to_jpg_page():
        from flask import render_template
        return render_template('index.html')  # Misma página que /
    
    @app.route('/pdf-a-png')
    @app.route('/pdf-to-png')  # Mantener compatibilidad
    def pdf_to_png_page():
        from flask import render_template
        return render_template('pdf_to_png.html')
    
    @app.route('/jpg-a-pdf')
    @app.route('/jpg-to-pdf')  # Mantener compatibilidad
    def jpg_to_pdf_page():
        from flask import render_template
        return render_template('jpg_to_pdf.html')
    
    # Páginas legales (requeridas por AdSense)
    @app.route('/privacy-policy')
    @app.route('/politica-de-privacidad')
    def privacy_policy():
        from flask import render_template
        return render_template('privacy_policy.html')
    
    @app.route('/terms')
    @app.route('/terminos')
    @app.route('/terms-of-service')
    def terms():
        from flask import render_template
        return render_template('terms.html')
    
    @app.route('/contact')
    @app.route('/contacto')
    def contact():
        from flask import render_template
        return render_template('contact.html')

    @app.route('/como-convertir-pdf')
    def como_convertir_pdf():
        from flask import render_template
        return render_template('como_convertir_pdf.html')

    # Registrar blueprints (rutas)
    # Para agregar nuevas herramientas, crear un nuevo archivo en routes/ y registrarlo aquí
    from app.routes import pdf_to_jpg, pdf_to_png, jpg_to_pdf, sitemap
    app.register_blueprint(pdf_to_jpg.bp)
    app.register_blueprint(pdf_to_png.bp)
    app.register_blueprint(jpg_to_pdf.bp)
    app.register_blueprint(sitemap.bp)
    
    # Ruta para robots.txt (desde raíz del proyecto para evitar bloqueos)
    @app.route('/robots.txt')
    def robots_txt():
        from flask import send_from_directory, Response
        import os
        path = os.path.join(base_dir, 'robots.txt')
        with open(path, 'r', encoding='utf-8') as f:
            body = f.read()
        r = Response(body, mimetype='text/plain')
        # Evitar caché para que Google siempre reciba la versión actual
        r.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        r.headers['Pragma'] = 'no-cache'
        r.headers['Expires'] = '0'
        return r
    
    # Ruta para ads.txt (requerido por Google AdSense)
    @app.route('/ads.txt')
    def ads_txt():
        from flask import send_from_directory
        import os
        return send_from_directory(
            os.path.join(base_dir, 'static'),
            'ads.txt',
            mimetype='text/plain'
        )
    
    return app

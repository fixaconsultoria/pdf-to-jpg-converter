"""
Punto de entrada principal de la aplicación.
Ejecutar este archivo para iniciar el servidor Flask.
"""
from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    # Configuración para desarrollo vs producción
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    # En producción, usar un servidor WSGI como Gunicorn
    # gunicorn -w 4 -b 0.0.0.0:5000 app:app
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        debug=debug_mode
    )

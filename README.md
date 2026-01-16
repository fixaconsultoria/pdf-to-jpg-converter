# Convertidor PDF a JPG Online

Aplicación web escalable para convertir archivos PDF a imágenes JPG. Diseñada con una arquitectura modular que permite agregar fácilmente nuevas herramientas de conversión.

## 🚀 Características

- ✅ Conversión de PDF a JPG de alta calidad (200 DPI)
- ✅ Soporte para PDFs de múltiples páginas
- ✅ Descarga automática en formato ZIP
- ✅ Limpieza automática de archivos temporales
- ✅ Sin registro ni autenticación requerida
- ✅ Interfaz responsive y moderna
- ✅ Optimizado para SEO
- ✅ Arquitectura escalable para nuevas herramientas

## 📋 Requisitos

- Python 3.8 o superior
- poppler-utils (requerido por pdf2image)

### Instalación de poppler

**macOS:**
```bash
brew install poppler
```

**Ubuntu/Debian:**
```bash
sudo apt-get install poppler-utils
```

**Windows:**
Descargar desde: https://github.com/oschwartz10612/poppler-windows/releases/
Y agregar al PATH del sistema.

## 🛠️ Instalación

1. Clonar o descargar el proyecto

2. Crear entorno virtual (recomendado):
```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## ▶️ Ejecución

### Desarrollo
```bash
python app.py
```

O con Flask directamente:
```bash
export FLASK_APP=app.py
export FLASK_DEBUG=True
flask run
```

La aplicación estará disponible en: `http://localhost:5000`

### Producción

Usar un servidor WSGI como Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 📁 Estructura del Proyecto

```
.
├── app/
│   ├── __init__.py          # Configuración Flask y factory
│   ├── routes/              # Endpoints por herramienta
│   │   ├── __init__.py
│   │   └── pdf_to_jpg.py    # Endpoint PDF a JPG
│   ├── utils/               # Utilidades reutilizables
│   │   ├── file_handler.py  # Gestión de archivos
│   │   └── converter.py     # Lógica de conversión
│   ├── uploads/             # Archivos temporales (auto-generado)
│   └── outputs/             # Archivos de salida (auto-generado)
├── static/
│   ├── css/
│   │   └── style.css        # Estilos
│   └── js/
│       └── main.js          # JavaScript principal
├── templates/
│   └── index.html           # Página principal
├── app.py                   # Punto de entrada
├── requirements.txt         # Dependencias Python
└── README.md               # Este archivo
```

## 🔧 Cómo Agregar Nuevas Herramientas

La arquitectura está diseñada para facilitar la adición de nuevas herramientas. Sigue estos pasos:

### 1. Crear función de conversión

En `app/utils/converter.py`, agrega tu nueva función:

```python
def pdf_to_png(pdf_path, output_folder, dpi=200):
    """Convierte PDF a PNG."""
    # Tu lógica aquí
    pass
```

### 2. Crear endpoint

Crea un nuevo archivo en `app/routes/`, por ejemplo `pdf_to_png.py`:

```python
from flask import Blueprint, request, jsonify, send_file
from app.utils.converter import pdf_to_png
from app.utils.file_handler import save_uploaded_file, create_zip_from_files

bp = Blueprint('pdf_to_png', __name__, url_prefix='/api/pdf-to-png')

@bp.route('/convert', methods=['POST'])
def convert_pdf_to_png():
    # Lógica similar a pdf_to_jpg.py
    pass
```

### 3. Registrar el blueprint

En `app/__init__.py`, agrega:

```python
from app.routes import pdf_to_png
app.register_blueprint(pdf_to_png.bp)
```

### 4. Crear página HTML (opcional)

Si quieres una página separada, crea `templates/pdf_to_png.html` y agrega una ruta en el blueprint.

### 5. Adaptar JavaScript (opcional)

Puedes reutilizar `static/js/main.js` cambiando solo el `API_ENDPOINT`.

## 🔒 Seguridad y Privacidad

- Los archivos se eliminan automáticamente después de 10 minutos
- No se almacenan archivos permanentemente
- Límite de tamaño: 20 MB por archivo
- Validación de tipos de archivo
- Sin almacenamiento de datos personales

## 📊 SEO

La aplicación está optimizada para SEO con:
- Meta tags descriptivos
- Títulos y encabezados semánticos
- Contenido descriptivo
- Estructura HTML clara
- Texto legal sobre privacidad

## 💰 Monetización Futura

La estructura está preparada para integrar Google AdSense:
- Comentarios en `index.html` indicando dónde agregar el código
- Área `.ad-container` en CSS lista para usar
- Descomentar el script de AdSense cuando tengas el código

## 🐛 Solución de Problemas

**Error: "poppler not found"**
- Asegúrate de tener poppler instalado y en el PATH

**Error: "File too large"**
- El límite es 20 MB. Comprime el PDF o divide el archivo.

**Error de conversión**
- Verifica que el PDF no esté corrupto
- Algunos PDFs protegidos pueden no funcionar

## 📝 Licencia

Este proyecto es de código abierto y está disponible para uso personal y comercial.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para agregar nuevas herramientas, sigue la estructura modular existente.

---

**Nota:** Esta aplicación está diseñada para producción pero recuerda:
- Cambiar `SECRET_KEY` en producción
- Configurar variables de entorno apropiadas
- Usar un servidor WSGI en producción (Gunicorn, uWSGI, etc.)
- Configurar HTTPS
- Ajustar límites según tus necesidades

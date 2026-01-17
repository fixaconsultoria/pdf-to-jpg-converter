# PDF Simple Convert - Herramientas de Conversión Online

Aplicación web para convertir archivos entre diferentes formatos. Diseñada con una arquitectura modular que permite agregar fácilmente nuevas herramientas de conversión.

## 🚀 Herramientas Disponibles

- ✅ **PDF a JPG** - Convierte PDFs a imágenes JPG de alta calidad
- ✅ **PDF a PNG** - Convierte PDFs a imágenes PNG sin compresión
- ✅ **JPG a PDF** - Combina múltiples imágenes JPG en un PDF

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

La aplicación estará disponible en: `http://localhost:5000`

### Producción

Usar un servidor WSGI como Gunicorn:

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 📁 Estructura del Proyecto

```
.
├── app/
│   ├── __init__.py          # Configuración Flask y factory
│   ├── routes/              # Endpoints por herramienta
│   │   ├── pdf_to_jpg.py    # Endpoint PDF a JPG
│   │   ├── pdf_to_png.py    # Endpoint PDF a PNG
│   │   ├── jpg_to_pdf.py    # Endpoint JPG a PDF
│   │   └── sitemap.py       # Generador de sitemap
│   ├── utils/               # Utilidades reutilizables
│   │   ├── file_handler.py  # Gestión de archivos
│   │   └── converter.py     # Lógica de conversión
│   ├── uploads/             # Archivos temporales (auto-generado)
│   └── outputs/             # Archivos de salida (auto-generado)
├── static/
│   ├── css/
│   │   └── style.css        # Estilos
│   ├── js/
│   │   └── main.js          # JavaScript principal
│   └── robots.txt           # Configuración SEO
├── templates/
│   ├── index.html           # Página principal (PDF a JPG)
│   ├── pdf_to_png.html      # Página PDF a PNG
│   ├── jpg_to_pdf.html      # Página JPG a PDF
│   ├── privacy_policy.html  # Política de privacidad
│   ├── terms.html           # Términos de servicio
│   └── contact.html         # Página de contacto
├── app.py                   # Punto de entrada
├── requirements.txt        # Dependencias Python
├── Dockerfile              # Configuración Docker
├── Procfile                # Configuración para deployment
├── runtime.txt             # Versión de Python
├── render.yaml             # Configuración Render.com
└── README.md               # Este archivo
```

## 🔒 Seguridad y Privacidad

- Los archivos se eliminan automáticamente después de 10 minutos
- No se almacenan archivos permanentemente
- Límite de tamaño: 20 MB por archivo
- Validación de tipos de archivo
- Sin almacenamiento de datos personales

## 📊 SEO

La aplicación está optimizada para SEO con:
- Meta tags descriptivos
- URLs SEO-friendly (`/pdf-a-jpg`, `/pdf-a-png`, `/jpg-a-pdf`)
- Sitemap.xml dinámico
- Robots.txt configurado
- Contenido original y de calidad (400+ palabras por página)
- Páginas legales completas

## 🌐 Deployment

El proyecto está configurado para deployment en Render.com:
- `Dockerfile` para contenedorización
- `render.yaml` para configuración de Render
- `Procfile` para ejecución con Gunicorn

## 📝 Licencia

Este proyecto es de código abierto y está disponible para uso personal y comercial.

---

**Nota:** Para producción:
- Cambiar `SECRET_KEY` en variables de entorno
- Configurar HTTPS
- Ajustar límites según necesidades

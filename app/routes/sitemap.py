"""
Generación dinámica de sitemap.xml para SEO
"""
from flask import Blueprint, Response, url_for, current_app
from datetime import datetime

bp = Blueprint('sitemap', __name__)

@bp.route('/sitemap.xml')
def sitemap():
    """Genera sitemap.xml dinámicamente con todas las páginas del sitio."""
    base_url = 'https://pdfsimpleconvert.com'
    
    # Lista de todas las páginas importantes
    pages = [
        {'url': '/', 'priority': '1.0', 'changefreq': 'daily'},
        {'url': '/pdf-a-jpg', 'priority': '0.9', 'changefreq': 'weekly'},
        {'url': '/pdf-a-png', 'priority': '0.9', 'changefreq': 'weekly'},
        {'url': '/jpg-a-pdf', 'priority': '0.9', 'changefreq': 'weekly'},
        {'url': '/como-convertir-pdf', 'priority': '0.8', 'changefreq': 'monthly'},
        {'url': '/privacy-policy', 'priority': '0.5', 'changefreq': 'monthly'},
        {'url': '/terms', 'priority': '0.5', 'changefreq': 'monthly'},
        {'url': '/contact', 'priority': '0.5', 'changefreq': 'monthly'},
    ]
    
    # Generar XML
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for page in pages:
        xml += '  <url>\n'
        xml += f'    <loc>{base_url}{page["url"]}</loc>\n'
        xml += f'    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>\n'
        xml += f'    <changefreq>{page["changefreq"]}</changefreq>\n'
        xml += f'    <priority>{page["priority"]}</priority>\n'
        xml += '  </url>\n'
    
    xml += '</urlset>'
    
    return Response(xml, mimetype='application/xml')

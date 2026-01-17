# Configuración de Google AdSense

## Estado Actual
✅ El sitio está preparado para integrar Google AdSense

## Estructura Preparada

### 1. Script de AdSense en `<head>`
Todas las páginas incluyen el script base de AdSense en el `<head>`:
```html
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXX" crossorigin="anonymous"></script>
```

**⚠️ ACCIÓN REQUERIDA:**
- Reemplazar `ca-pub-XXXXXXXXXX` con tu Publisher ID real de Google AdSense
- Este ID se obtiene después de la aprobación de tu cuenta en AdSense

### 2. Ubicaciones de Anuncios Preparadas

#### Páginas de Herramientas (index.html, pdf_to_png.html, jpg_to_pdf.html):
- **Banner superior**: Después del contenedor de la herramienta, antes del contenido informativo
- **Banner inferior**: Después del contenido informativo, antes del footer

#### Páginas Legales (privacy_policy.html, terms.html, contact.html):
- Solo script en `<head>` (sin unidades de anuncio visibles aún)

### 3. Cumplimiento de Políticas de AdSense

✅ **Verificado:**
- No hay anuncios cerca de botones de subida/descarga
- No hay popups invasivos
- Contenido original y de calidad en cada página (200-300 palabras)
- Páginas legales completas (Privacy Policy, Terms, Contact)
- Navegación clara y estructura profesional
- URLs SEO-friendly

### 4. Pasos para Activar AdSense

1. **Solicitar aprobación en Google AdSense:**
   - Visita: https://www.google.com/adsense/
   - Crea una cuenta o inicia sesión
   - Agrega tu sitio: `https://pdfsimpleconvert.com`
   - Completa el proceso de verificación

2. **Obtener tu Publisher ID:**
   - Después de la aprobación, obtendrás un ID como: `ca-pub-1234567890123456`

3. **Reemplazar en todas las páginas:**
   - Buscar y reemplazar: `ca-pub-XXXXXXXXXX`
   - Con tu ID real: `ca-pub-TU_ID_REAL`

4. **Agregar unidades de anuncio (opcional):**
   - Después de la aprobación, puedes crear unidades de anuncio en el panel de AdSense
   - Reemplazar `data-ad-slot="XXXXXXXXXX"` con los slots reales
   - O usar formato automático (ya configurado)

### 5. Archivos que Requieren Actualización

Una vez aprobado, actualizar estos archivos:
- `templates/index.html` (líneas 14, 82, 125)
- `templates/pdf_to_png.html` (líneas 11, 78, 110)
- `templates/jpg_to_pdf.html` (líneas 11, 115)
- `templates/privacy_policy.html` (línea 10)
- `templates/terms.html` (línea 10)
- `templates/contact.html` (línea 10)

### 6. Mejores Prácticas Implementadas

✅ Anuncios no bloquean contenido principal
✅ Anuncios no están cerca de botones de acción
✅ Contenido de calidad antes de mostrar anuncios
✅ Estructura clara y navegación intuitiva
✅ Páginas legales accesibles desde footer
✅ Contenido original y útil en cada página

### 7. Notas Importantes

- **No activar anuncios hasta obtener aprobación**: Los anuncios actuales son placeholders
- **Esperar aprobación antes de monetizar**: Google puede tardar varios días en revisar
- **Mantener contenido de calidad**: Continuar agregando herramientas y contenido útil
- **Monitorear rendimiento**: Una vez activo, revisar métricas en el panel de AdSense

## Checklist Pre-Aprobación

- [x] Contenido original y de calidad (200+ palabras por página)
- [x] Páginas legales completas (Privacy, Terms, Contact)
- [x] Navegación clara y estructura profesional
- [x] URLs SEO-friendly
- [x] Sitemap.xml y robots.txt configurados
- [x] Sin popups invasivos
- [x] Anuncios no cerca de botones de acción
- [x] Sitio funcional y sin errores
- [ ] Reemplazar Publisher ID después de aprobación
- [ ] Activar unidades de anuncio después de aprobación

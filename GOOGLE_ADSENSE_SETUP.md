# 📢 Guía: Integrar Google AdSense

## ✅ Lo que ya está hecho:

1. ✅ Código de AdSense agregado en `index.html`
2. ✅ Bloques de anuncios preparados (2 ubicaciones)
3. ✅ CSS listo para los contenedores de anuncios

## 🔧 Pasos para activar AdSense:

### Paso 1: Obtener código de AdSense

1. **Ir a:** https://www.google.com/adsense/
2. **Iniciar sesión** con tu cuenta de Google
3. **Crear cuenta** (si no tienes una)
4. **Agregar tu sitio web:**
   - URL: `tu-url.onrender.com`
   - Ejemplo: `pdf-to-jpg-converter-qz7s.onrender.com`

### Paso 2: Obtener Publisher ID

1. En AdSense, ve a **"Sitios"** o **"Sites"**
2. Copia tu **Publisher ID** (formato: `ca-pub-XXXXXXXXXX`)

### Paso 3: Crear unidades de anuncios

1. Ve a **"Anuncios"** → **"Por unidad"** → **"Crear nueva unidad"**
2. Elige tipo: **"Pantalla"** (Display ads)
3. Formato: **"Responsive"** o **"Automático"**
4. Copia el **Slot ID** (formato: `XXXXXXXXXX`)

### Paso 4: Reemplazar en el código

**En todos los archivos HTML** (`index.html`, `pdf_to_png.html`, `jpg_to_pdf.html`):

1. **Reemplazar `ca-pub-XXXXXXXXXX`** con tu Publisher ID real
2. **Reemplazar `data-ad-slot="XXXXXXXXXX"`** con tu Slot ID real

**Ejemplo:**
```html
<!-- ANTES -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXX" crossorigin="anonymous"></script>

<!-- DESPUÉS (con tu ID real) -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1234567890123456" crossorigin="anonymous"></script>
```

Y en los bloques de anuncios:
```html
<!-- ANTES -->
data-ad-client="ca-pub-XXXXXXXXXX"
data-ad-slot="XXXXXXXXXX"

<!-- DESPUÉS (con tus IDs reales) -->
data-ad-client="ca-pub-1234567890123456"
data-ad-slot="9876543210"
```

### Paso 5: Aplicar en todas las páginas

**Archivos a modificar:**
- `templates/index.html`
- `templates/pdf_to_png.html`
- `templates/jpg_to_pdf.html`

**En cada archivo buscar y reemplazar:**
- Publisher ID: `ca-pub-XXXXXXXXXX` → `ca-pub-TU-ID-REAL`
- Slot ID: `XXXXXXXXXX` → `TU-SLOT-ID-REAL`

### Paso 6: Commit y Deploy

1. **Commit:** "Integrar Google AdSense"
2. **Push a GitHub**
3. **Render hará deploy automático**

### Paso 7: Verificar en AdSense

1. AdSense puede tardar **24-48 horas** en aprobar tu sitio
2. Mientras tanto, verás anuncios de prueba o espacios en blanco
3. Una vez aprobado, comenzarás a ver anuncios reales

## 📍 Ubicaciones de los anuncios:

1. **Banner superior:** Después del área de conversión
2. **Banner inferior:** Antes del footer

## ⚠️ Importante:

- **No hagas clic en tus propios anuncios** (viola las políticas)
- **Espera la aprobación** de Google (puede tardar días)
- **Mantén el tráfico orgánico** (no compres tráfico falso)
- **Cumple con las políticas** de AdSense

## 🎯 Optimización:

- Los anuncios son **responsive** (se adaptan al tamaño de pantalla)
- Ubicados en **zonas visibles** pero no intrusivas
- **No bloquean** la funcionalidad principal

---

**¿Necesitas ayuda con algún paso específico?**

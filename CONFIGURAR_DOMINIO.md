# 🌐 Guía: Configurar Dominio Personalizado en Render

## ✅ Ventajas de tener dominio propio:

- ✅ Más profesional y confiable
- ✅ Mejor para SEO
- ✅ Google AdSense prefiere dominios propios
- ✅ Más fácil de recordar
- ✅ SSL/HTTPS automático

## 📋 Pasos para configurar dominio:

### Paso 1: Comprar Dominio

**Proveedores recomendados:**
- **Namecheap** - $8-12/año (recomendado)
- **Google Domains** - $12/año
- **GoDaddy** - $10-15/año
- **Cloudflare** - $8-10/año

**Ejemplos de dominios:**
- `convertirpdf.com`
- `pdfonline.es`
- `convertidor-pdf.com`
- `pdfherramientas.com`
- `convertir-pdf.online`

### Paso 2: En Render - Agregar Dominio

1. **Ve a Render Dashboard**
2. **Abre tu servicio:** "pdf-to-jpg-converter"
3. **Ve a "Settings"** (Ajustes)
4. **Busca "Custom Domains"** o "Dominios personalizados"
5. **Click en "Add Custom Domain"** o **"+ Add"**
6. **Ingresa tu dominio:** `tu-dominio.com` (sin www)
7. **Render te mostrará registros DNS a configurar**

### Paso 3: Configurar DNS en tu Proveedor

**En tu proveedor de dominio (Namecheap, GoDaddy, etc.):**

#### Opción A: Usar CNAME (Más fácil)

1. Ve a la sección **"DNS"** o **"DNS Management"**
2. **Agrega un registro CNAME:**
   - **Host/Name:** `@` o `www` (o ambos)
   - **Value/Target:** `[tu-app].onrender.com` (Render te dará esto exacto)
   - **TTL:** 3600 (o automático)

#### Opción B: Usar A Record

1. **Agrega registro A:**
   - **Host/Name:** `@`
   - **Value/IP:** `76.76.21.21` (IP de Render - puede variar)
   - **TTL:** 3600

**Render te dará las instrucciones exactas después de agregar el dominio.**

### Paso 4: Esperar Propagación DNS

- DNS puede tardar **5 minutos a 48 horas** en propagarse
- Normalmente toma **15-30 minutos**
- Puedes verificar con: https://www.whatsmydns.net/

### Paso 5: Verificar en Render

1. Render verificará automáticamente el dominio
2. Una vez verificado, aparecerá como "Active"
3. **SSL/HTTPS se configura automáticamente** (puede tardar unos minutos)

### Paso 6: Verificar SSL

1. Una vez que Render configure SSL, verás un candado 🔒
2. Tu sitio funcionará en: `https://tu-dominio.com`
3. También funcionará en: `https://www.tu-dominio.com` (si configuraste www)

## ⚙️ Configuración Adicional:

### Redirección www a no-www (o viceversa)

**En Render Settings → Redirects:**
- Opcional: Configurar redirección automática
- Ejemplo: `www.tu-dominio.com` → `tu-dominio.com`

### Verificar que funciona

1. Visita: `https://tu-dominio.com`
2. Debe cargar tu aplicación
3. Debe mostrar el candado SSL (🔒)

## 🔄 Actualizar código si es necesario

Una vez que tengas el dominio:

1. **Actualizar variables de entorno** (si usas dominio en código)
2. **Actualizar meta tags** (opcional, para SEO)
3. **Revisar que todas las rutas funcionan**

## 📝 Checklist:

- [ ] Dominio comprado
- [ ] DNS configurado en proveedor
- [ ] Dominio agregado en Render
- [ ] DNS propagado (verificado)
- [ ] SSL/HTTPS activo
- [ ] Sitio accesible en nuevo dominio
- [ ] Verificar que funciona correctamente

## ⏱️ Tiempo estimado:

- **Comprar dominio:** 5 minutos
- **Configurar DNS:** 5 minutos
- **Propagación DNS:** 15 minutos - 48 horas (normalmente 30 min)
- **SSL automático:** 5-10 minutos después de DNS

**Total:** ~1 hora (normalmente menos)

---

**Una vez que tengas el dominio funcionando, entonces solicitas Google AdSense con el dominio propio.**

¿Ya tienes un dominio o necesitas comprarlo?

# 🔍 ¿Dónde Están las Opciones en Render?

## Si NO ves "Build & Deploy":

### Opción 1: Buscar en la página principal del servicio

1. **Ve a tu servicio:** "pdf-to-jpg-converter"
2. **NO entres a Settings**, quédate en la página principal
3. **Busca en la parte superior o media:**
   - Sección que dice **"Environment"** o **"Entorno"**
   - O **"Build Settings"**
   - O campos que digan **"Build Command"** y **"Start Command"**

### Opción 2: Buscar en la parte superior del servicio

En la página principal del servicio, arriba suele haber:
- Botones o pestañas: **"Overview"**, **"Logs"**, **"Metrics"**, **"Settings"**
- A veces **"Environment"** está visible directamente

### Opción 3: Buscar "Environment" directamente

1. En el menú lateral izquierdo (sidebar)
2. **Busca "Environment"** o **"Environment Variables"**
3. Ahí suelen estar Build Command y Start Command

### Opción 4: En la configuración del entorno

1. Click en el nombre del **entorno** (arriba, tipo "Production" o "producción")
2. O busca **"Environment Settings"**

## 📸 Qué Buscar Exactamente:

Busca campos que digan:
- **"Build Command"** (comando de construcción)
- **"Start Command"** (comando de inicio)
- **"Environment"** (entorno)
- **"Python Version"** (versión de Python)

## 🎯 Alternativa: Usar render.yaml

Si no encuentras las opciones en la interfaz, podemos usar el archivo `render.yaml` que ya creamos.

1. **Sube render.yaml a GitHub:**
   - Ya lo tenemos creado
   - Haz push a GitHub

2. **Render puede detectarlo automáticamente**
   - O puedes indicarle a Render que use ese archivo

## ❓ ¿Qué VES en Settings?

Dime qué opciones/sections ves en Settings:
- ¿Ves "Environment Variables"?
- ¿Ves "Deploy"?
- ¿Ves "Scaling"?
- ¿Ves algo relacionado con "Environment" o "Entorno"?

---

**Dime exactamente qué ves en la pantalla y te guío mejor.**

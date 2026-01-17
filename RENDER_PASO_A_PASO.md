# 🚀 Render - Guía Paso a Paso COMPLETA

## 📋 Pasos Exactos (Sigue en Orden)

### PASO 1: Ve a Settings

1. En Render Dashboard, ve a tu servicio: **"pdf-to-jpg-converter"**
2. **Click en "Settings"** (Ajustes) - Está en el menú superior

### PASO 2: Configurar Build & Deploy

En la sección **"Build & Deploy"**:

#### 2.1: Build Command
- **Busca "Build Command"**
- **ELIMINA completamente** lo que dice actualmente
- **DEJALO VACÍO** (sin nada)

#### 2.2: Start Command  
- **Busca "Start Command"**
- **Escribe exactamente:** 
  ```
  gunicorn app:app
  ```

#### 2.3: Environment
- Debe decir: **"Python 3"** (no lo cambies si ya dice eso)

### PASO 3: Buscar Opción Docker

**EN LA MISMA SECCIÓN "Build & Deploy":**

1. **Busca si hay:**
   - Opción **"Use Dockerfile"**
   - O **"Docker"**
   - O **"Dockerfile Path"**

2. **SI encuentras alguna opción Docker:**
   - ✅ **ACTÍVALA**
   - Si pide ruta, pon: `Dockerfile`

3. **SI NO encuentras opción Docker:**
   - ⚠️ El plan gratuito puede no tenerlo
   - **Sigue al PASO 4** (solución alternativa)

### PASO 4: Variables de Entorno

1. **En Settings, busca "Environment Variables"**
2. **Click en "Add Environment Variable"** (puede estar como "+ Add" o "Add Variable")
3. **Agrega estas 3 variables, UNA POR UNA:**

   **Variable 1:**
   - Key: `SECRET_KEY`
   - Value: `cc047147136cc646a1f0c57d689d1165dd1bafbf70d6b3201be4435ad11ce08d`
   - Click "Save"

   **Variable 2:**
   - Key: `FLASK_ENV`
   - Value: `production`
   - Click "Save"

   **Variable 3:**
   - Key: `FLASK_DEBUG`
   - Value: `False`
   - Click "Save"

### PASO 5: Si NO hay Docker - Solución Alternativa

Si Render NO tiene opción Docker, tenemos que modificar el approach:

**Opción A: Instalar poppler después del deploy**
- No es ideal pero puede funcionar
- Requiere modificar el código

**Opción B: Usar servicio externo para conversión**
- Más complejo

**Opción C: Actualizar plan Render ($7/mes)**
- Tendrá acceso a Docker

### PASO 6: Guardar y Deploy

1. **Desplázate hacia abajo** en Settings
2. **Click en "Save Changes"** (si hay botón)
3. **O simplemente ve a la pestaña "Events" o "Logs"**

4. **Para redeploy:**
   - Ve a **"Manual Deploy"** (arriba)
   - O busca **"Deploy latest commit"**
   - **Click en "Deploy"**

### PASO 7: Ver Logs

1. **Ve a la pestaña "Logs"**
2. **Observa el progreso:**
   - ✅ Si ves "Building..."
   - ✅ Si ves "Installing dependencies..."
   - ✅ Si ves "Starting gunicorn..."
   - ✅ Si ves "Listening on port..."

3. **Si hay error:**
   - Copia el mensaje de error
   - Te ayudo a solucionarlo

## ❓ Si Ves Este Error:

### Error: "poppler not found"

**Solución temporal (sin Docker):**
Necesitamos cambiar el código para que Render instale poppler de otra manera.

Te ayudo a modificar el código si Render no tiene Docker disponible.

## ✅ Checklist

- [ ] Build Command: VACÍO
- [ ] Start Command: `gunicorn app:app`
- [ ] Variables de entorno agregadas (3)
- [ ] Docker activado (si está disponible)
- [ ] Deploy iniciado
- [ ] Logs verificados

---

**Empieza con PASO 1 y sigue en orden. Si te atascas en algún paso, dime exactamente dónde estás y qué ves en la pantalla.**

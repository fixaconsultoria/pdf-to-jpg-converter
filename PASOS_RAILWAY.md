# 🚂 Guía: Desplegar en Railway

## Paso 1: Crear Nuevo Proyecto

1. En Railway, haz click en el botón **"+ Nuevo"** (arriba a la derecha)
2. O haz click en el icono de **GitHub** en la sección "Crear un nuevo proyecto"

## Paso 2: Conectar GitHub

1. Railway te pedirá autorizar acceso a GitHub
2. Click en **"Authorize Railway"** o **"Autorizar Railway"**
3. Selecciona la organización **"fixaconsultoria"**
4. Autoriza el acceso

## Paso 3: Seleccionar Repositorio

1. Busca y selecciona: **"pdf-to-jpg-converter"**
2. Railway detectará automáticamente que es Python/Flask
3. Click en **"Deploy"** o **"Desplegar"**

## Paso 4: Configurar Variables de Entorno

**IMPORTANTE:** Después de que Railway empiece a desplegar:

1. Ve a la pestaña **"Variables"** o **"Variables de entorno"**
2. Agrega estas variables:

   ```
   SECRET_KEY = cc047147136cc646a1f0c57d689d1165dd1bafbf70d6b3201be4435ad11ce08d
   FLASK_ENV = production
   FLASK_DEBUG = False
   ```

3. Guarda los cambios

## Paso 5: Configurar Build (Si es necesario)

Railway debería detectar automáticamente:
- ✅ Python
- ✅ requirements.txt
- ✅ Procfile

Si no detecta, en **Settings** → **Build**:
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

## Paso 6: Instalar poppler-utils

**IMPORTANTE:** Railway necesita poppler-utils para convertir PDFs.

1. Ve a **Settings** → **Service**
2. Busca **"Build Command"** o crea un archivo `railway.json`:

```json
{
  "build": {
    "builder": "NIXPACKS",
    "buildCommand": "apt-get update && apt-get install -y poppler-utils && pip install -r requirements.txt"
  }
}
```

O más fácil, agrega al inicio de `requirements.txt`:
```
# Instalar poppler-utils primero
```

**Mejor opción:** Crear archivo `nixpacks.toml` en la raíz:

```toml
[phases.setup]
nixPkgs = ["poppler_utils"]
```

## Paso 7: Esperar el Deploy

- Railway construirá y desplegará automáticamente
- Verás logs en tiempo real
- Cuando termine, tendrás una URL pública

## Paso 8: Probar la Aplicación

1. Railway te dará una URL tipo: `tu-app.railway.app`
2. Abre la URL en el navegador
3. Prueba subir un PDF

## ⚠️ Problemas Comunes

### Error: "poppler not found"
- Agrega `nixpacks.toml` con la configuración de poppler
- O usa un buildpack personalizado

### Error: "Module not found"
- Verifica que `requirements.txt` tenga todas las dependencias
- Revisa los logs de build

### Error: "Port already in use"
- Railway maneja esto automáticamente
- No necesitas configurar puerto manualmente

## ✅ Checklist

- [ ] Proyecto creado en Railway
- [ ] GitHub conectado
- [ ] Repositorio seleccionado
- [ ] Variables de entorno configuradas
- [ ] poppler-utils instalado (nixpacks.toml)
- [ ] Deploy completado
- [ ] URL funcionando

---

**¿Necesitas ayuda con algún paso?** Railway es bastante automático, pero si hay problemas, revisa los logs.

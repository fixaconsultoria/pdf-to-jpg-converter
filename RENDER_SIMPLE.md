# 🎯 Solución SIMPLE para Render

## El Problema
Render no permite `apt-get` en el build command.

## Solución SUPER Simple

### Paso 1: En Render Dashboard

1. Ve a tu servicio: **"pdf-to-jpg-converter"**
2. Click en **"Settings"** (Ajustes, arriba)
3. Busca **"Build & Deploy"**

### Paso 2: ELIMINAR el Build Command

**En "Build Command":**
- **BORRA TODO** lo que dice ahí
- **DEJALO COMPLETAMENTE VACÍO**

**En "Start Command":**
- Pon solo: `gunicorn app:app`

### Paso 3: Para poppler-utils - Usar Docker

**Busca en Settings:**
- Opción **"Docker"** o **"Use Dockerfile"**
- **ACTÍVALA**
- Render usará tu Dockerfile automáticamente

**Si NO ves opción Docker:**
- Render puede no tenerla en el plan gratuito
- En ese caso, necesitarás actualizar el plan o usar otra opción

### Paso 4: Variables de Entorno

En **"Environment Variables"**, agrega:
```
SECRET_KEY = cc047147136cc646a1f0c57d689d1165dd1bafbf70d6b3201be4435ad11ce08d
FLASK_ENV = production
FLASK_DEBUG = False
```

### Paso 5: Redeploy

- Click en **"Manual Deploy"**
- **"Deploy latest commit"**

---

## Si Render NO tiene opción Docker

**Opción A:** Actualizar plan de Render ($7/mes)
**Opción B:** Usar VPS DigitalOcean ($5/mes) - más barato y funciona perfecto
**Opción C:** Probar localmente primero

---

**¿Qué opción prefieres?** Puedo ayudarte con cualquiera.

# 🔧 Fix: Build Command en Render

## Si Render NO permite Build Command vacío:

### Build Command (pon esto):
```
pip install -r requirements.txt
```

### Start Command:
```
gunicorn app:app
```

## ⚠️ Problema: poppler-utils

Con este build command, **NO se instalará poppler-utils** porque Render no permite `apt-get`.

## ✅ Soluciones para poppler-utils:

### Opción 1: Verificar si hay Docker (MEJOR)

1. En Settings → Build & Deploy
2. **Busca si hay:**
   - "Docker" 
   - "Use Dockerfile"
   - "Dockerfile Path"
   - "Container"
3. **Si encuentras alguna opción:**
   - ✅ **ACTÍVALA**
   - Render usará tu Dockerfile (que SÍ tiene poppler-utils)

### Opción 2: Si NO hay Docker - Modificar código

Si Render no tiene Docker, necesitamos una solución alternativa.

**Opción A:** Usar un servicio externo para conversión
**Opción B:** Actualizar plan Render ($7/mes) para tener Docker
**Opción C:** Usar otra plataforma

---

## 🎯 Pasos Inmediatos:

1. **Build Command:** `pip install -r requirements.txt`
2. **Start Command:** `gunicorn app:app`
3. **Buscar opción Docker** en Settings
4. **Si encuentras Docker:** Actívalo
5. **Si NO encuentras Docker:** Dime y te ayudo con alternativa

---

**¿Ves alguna opción relacionada con Docker en Settings?**

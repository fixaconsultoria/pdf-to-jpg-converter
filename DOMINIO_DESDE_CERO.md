# 🌐 Dominio en Render + Porkbun - Desde Cero

Guía paso a paso para configurar **pdfsimpleconvert.com** desde el principio.

---

## PARTE 1: RENDER

### Paso 1.1: Ir a Custom Domains

1. Entra a **https://dashboard.render.com**
2. Abre tu servicio **"pdf-to-jpg-converter"**
3. En el menú izquierdo, haz clic en **"Settings"**
4. En el panel derecho, busca y haz clic en **"Custom Domains"**

### Paso 1.2: Limpiar dominios anteriores (si los hay)

Si ya tienes **pdfsimpleconvert.com** o **www.pdfsimpleconvert.com**:

1. En cada uno, haz clic en **"Delete"** (rojo)
2. Confirma
3. Deja la sección **Custom Domains** sin ningún dominio

### Paso 1.3: Agregar el dominio CON www PRIMERO

1. Haz clic en **"+ Add Custom Domain"**
2. Escribe **exactamente:** `www.pdfsimpleconvert.com`
3. Haz clic en **"Add"** / **"Save"**
4. Render mostrará algo como:
   - **"Add a CNAME record"**
   - **Host:** `www`
   - **Value/Points to:** `pdf-to-jpg-converter-qz7s.onrender.com`
   - (Anota este valor por si acaso)

### Paso 1.4: Agregar el dominio SIN www (raíz)

1. Haz clic de nuevo en **"+ Add Custom Domain"**
2. Escribe **exactamente:** `pdfsimpleconvert.com` (sin www)
3. Haz clic en **"Add"** / **"Save"**
4. Render mostrará **una de estas dos** opciones:

   **Opción A – ANAME/ALIAS:**
   - Add an **ANAME** or **ALIAS** record
   - **Points to:** `pdf-to-jpg-converter-qz7s.onrender.com`

   **Opción B – A record (si no hay ALIAS):**
   - Add an **A** record
   - **Points to:** `216.24.57.1` (o la IP que Render indique)

Anota bien qué pide Render (ALIAS o A) y el valor.

---

## PARTE 2: PORKBUN – Limpiar DNS

### Paso 2.1: Entrar a DNS del dominio

1. Entra a **https://porkbun.com**
2. Inicia sesión
3. Ve a **"Account"** → **"Domain Management"** (o "Domains")
4. Haz clic en **pdfsimpleconvert.com**
5. Busca **"DNS"** o **"Edit DNS"** o **"DNS Records"** y ábrelo

### Paso 2.2: Borrar registros que sobran

Borra **solo** estos (si existen):

- Cualquier **ALIAS** o **ANAME** cuyo HOST sea `@`, `pdfsimpleconvert.com` o similar
- Cualquier **CNAME** cuyo HOST sea `www`
- Cualquier **A** con HOST `@` que apunte a una IP de Render u otra

**No borres:**
- **MX** (fwd1.porkbun.com, fwd2.porkbun.com)
- **TXT** con `v=spf1 include:_spf.porkbun.com ~all`
- **TXT** `_acme-challenge` (opcional: si quieres empezar muy limpio, también puedes borrarlos; Render los creará de nuevo al pedir el certificado)

Para borrar: icono de **papelera** en cada registro.

---

## PARTE 3: PORKBUN – Crear los 2 registros correctos

Solo necesitas **2 registros nuevos** para Render.

---

### Registro 1: CNAME para www (www.pdfsimpleconvert.com)

1. Haz clic en **"Add"** / **"Add Record"** / **"Añadir registro"**
2. Rellena:

   | Campo            | Valor                                              |
   |------------------|----------------------------------------------------|
   | **Type / Tipo**  | `CNAME`                                            |
   | **Host / Anfitrión** | `www`                                          |
   | **Answer / Respuesta** | `pdf-to-jpg-converter-qz7s.onrender.com`   |
   | **TTL**          | `600`                                              |

3. **Priority** y **Notes** → vacíos
4. Guarda (**"Add"** / **"Agregar"**)

---

### Registro 2: ALIAS o A para el dominio raíz (pdfsimpleconvert.com)

Elige **una** de las dos, según lo que Render te haya dicho.

#### OPCIÓN A – Si Render pide ALIAS/ANAME

1. **"Add"** / **"Add Record"**
2. Rellena:

   | Campo            | Valor                                              |
   |------------------|----------------------------------------------------|
   | **Type / Tipo**  | `ALIAS` (o `ANAME` si solo existe eso)             |
   | **Host / Anfitrión** | `@` **o déjalo en blanco** (para dominio raíz) |
   | **Answer / Respuesta** | `pdf-to-jpg-converter-qz7s.onrender.com`   |
   | **TTL**          | `600`                                              |

3. Guarda

#### OPCIÓN B – Si Render pide A o si ALIAS falla

1. **"Add"** / **"Add Record"**
2. Rellena:

   | Campo            | Valor                                              |
   |------------------|----------------------------------------------------|
   | **Type / Tipo**  | `A`                                                |
   | **Host / Anfitrión** | `@` **o en blanco**                           |
   | **Answer / Respuesta** | `216.24.57.1`                              |
   | **TTL**          | `600`                                              |

3. Guarda

(La IP `216.24.57.1` es la que Render suele indicar; si en tu pantalla sale otra, usa esa.)

---

## PARTE 4: Comprobar en Porkbun

Tu zona debe tener algo así (además de MX y TXT que no tocaste):

| TYPE  | HOST | ANSWER                                  |
|-------|------|-----------------------------------------|
| CNAME | www  | pdf-to-jpg-converter-qz7s.onrender.com  |
| ALIAS | @    | pdf-to-jpg-converter-qz7s.onrender.com  |

**o**, en lugar de ALIAS:

| TYPE | HOST | ANSWER      |
|------|------|-------------|
| A    | @    | 216.24.57.1 |

---

## PARTE 5: Verificar en Render

1. Espera **5–10 minutos**
2. En **Render** → **Settings** → **Custom Domains**
3. Para **www.pdfsimpleconvert.com**:
   - Si hay botón **"Verify"**, haz clic
   - Debe pasar a: ✓ Domain Verified, ✓ Certificate Issued
4. Para **pdfsimpleconvert.com**:
   - Igual: **"Verify"** si existe
   - Debe pasar a: ✓ Domain Verified, ✓ Certificate Issued

Si uno tarda más, espera hasta 1 hora y vuelve a **Verify**.

---

## PARTE 6: Probar en el navegador

Abre:

- **https://www.pdfsimpleconvert.com**  
- **https://pdfsimpleconvert.com**

Los dos deben cargar tu aplicación y mostrar el candado (HTTPS).

---

## Resumen rápido

1. **Render:** Borrar dominios viejos → Añadir `www.pdfsimpleconvert.com` → Añadir `pdfsimpleconvert.com`
2. **Porkbun:** Borrar ALIAS/CNAME/A viejos de `@` y `www` → Crear CNAME `www` → Render → Crear ALIAS `@` → Render **o** A `@` → `216.24.57.1`
3. Esperar 5–10 min (o hasta 1 h) → **Verify** en Render → Probar las dos URLs

---

## Si algo falla

- **Solo www funciona, el raíz no:** Revisa que el ALIAS o A con HOST `@` esté bien y que no haya otro A/ALIAS para `@` que lo pise.
- **"Could not edit DNS record" en Porkbun:** No edites; borra el registro y créalo de nuevo con **Add**.
- **Certificate Error en Render:** Espera 1 hora, **Verify** otra vez; si sigue, Contact support en Render.

# 📦 Generador y Lector de Códigos de Barras (EAN-13) con Python Sencillo 

Esta aplicación permite generar **códigos de barras tipo supermercado (EAN-13)** a partir de un número, y también escanear códigos de barras físicos usando la **cámara del dispositivo**. Incluye una interfaz gráfica creada con `Tkinter`.

---

## 🖼️ Características

- ✅ Generación de códigos de barras EAN-13 (formato usado en supermercados).
- ✅ Escaneo en vivo con la cámara (lectura de códigos 1D).
- ✅ Interfaz gráfica amigable.
- ✅ Vista previa del código generado.
- ✅ Detección de código escaneado con OpenCV y Pyzbar.
---

## 🚀 Requisitos

Instala las dependencias necesarias con:

```bash
pip install python-barcode pillow opencv-python pyzbar
```

---

## 🧪 Cómo usar

### 🔘 Generar código de barras:

1. Escribe un número de **12 o 13 dígitos** (válido para EAN-13).
2. Presiona el botón **"Generar Código de Barras"**.
3. Se mostrará una imagen con el código generado.

### 📷 Escanear con la cámara:

1. Presiona el botón **"Leer Código con Cámara"**.
2. Se abrirá una ventana con la cámara.
3. Apunta al **código de barras físico** para leerlo.
4. El contenido escaneado aparecerá en la interfaz.
5. Presiona `ESC` para cerrar la ventana de la cámara.

---

## ⚠️ Consideraciones

- Asegúrate de que **tu cámara no esté siendo utilizada por otro programa**.
- En algunos entornos Windows, es necesario **forzar el backend `cv2.CAP_DSHOW`** para que funcione correctamente con OpenCV.

---

## 📄 Licencia

MIT License. Puedes usar este código libremente en proyectos personales o comerciales, con o sin modificaciones.

---

## ✨ Autor

Desarrollado por **SystemsBM**.



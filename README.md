# 🌳 Juego de Aventuras Interactivo en Python

## 👥 Integrantes del Grupo

- Cristian Ariel Morales - 
- Benito Sebastian Rios - 

## 🏫 Comisión

- Comisión: 2025-04

## 📘 Presentación del Tema

Este proyecto implementa un juego de aventuras interactivo utilizando la estructura de árbol binario representada mediante listas en Python. Cada nodo representa una decisión o un final dentro de la historia, lo que permite construir narrativas ramificadas y personalizadas.

El jugador debe tomar decisiones a medida que avanza por los nodos, con la posibilidad de perder vidas si elige caminos incorrectos, lo que añade un componente lúdico y estratégico.

## 🎯 Objetivos del Proyecto

- Implementar una estructura de árbol binario con listas anidadas en Python.
- Desarrollar un sistema de juego basado en decisiones jerárquicas.
- Permitir la creación personalizada de aventuras por parte del usuario.
- Aplicar conceptos de recorrido de árboles (preorden, inorden, postorden) para visualizar la narrativa.
- Incorporar persistencia de datos mediante archivos para guardar y cargar aventuras.

## 🔗🎥 PDF Entregable

👉 [Ver PDF](https://drive.google.com/file/d/11f_0-rg16t7WBGmhTt4Zjxm8rbT7nHE4/view?usp=drive_link)

## 🔗🎥 Presentación

👉 [Ver PDF](https://drive.google.com/file/d/1K4hbBif0mxw6UD4hvdCu05u9TtWzPA2H/view?usp=drive_link)

## 🔗🎥 Enlace al video explicativo

👉 [Ver video en YouTube](https://www.youtube.com/watch?v=1WbyTA41EUU)

---

## 🛠️ Modo de Uso

### 1. Clonar el repositorio o descargar el código fuente

```bash
git clone https://github.com/usuario/proyecto-aventuras-python.git
cd proyecto-aventuras-python
```
📦 Alternativamente, podés descargar el archivo .zip desde GitHub y descomprimirlo.

### 2. Ejecutar el programa principal

Asegurate de tener Python 3 instalado en tu sistema.
Para iniciar el programa, ejecutá el archivo principal:

```bash
python main.py
```
### 3. Navegar por el menú principal

Una vez iniciado, el programa mostrará un menú interactivo con las siguientes opciones:

1. Crear aventura nueva: Construí tu propia historia definiendo preguntas y finales.
2. Jugar aventura: Elegí una historia y tomá decisiones para avanzar.
3. Ver aventura: Explorá la estructura del árbol en diferentes tipos de recorridos:
    - Preorden
    - Inorden
    - Postorden
4. Salir: Finaliza la ejecución del programa.

### 4. Guardar y cargar aventuras

- 🗂 Las aventuras se almacenan como archivos .json en la carpeta aventuras/.
- 📌 Se pueden crear, guardar y jugar múltiples historias.
- 🧹 Para eliminar una historia, basta con borrar su archivo .json.
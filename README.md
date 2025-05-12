
![Logo del proyecto](./images/dmj.jpg)

# 🧙‍♂️ Dungeon Master AI

¿Alguna vez has soñado con tener tu propio Dungeon Master para tus partidas de *Dragones y Mazmorras*? ¡Ahora es posible! Esta aplicación, desarrollada con la API de OpenAI y Streamlit, te permite disfrutar de aventuras personalizadas, gestionar encuentros y vivir una experiencia única en cada sesión.

## 🚀 Características

- **Narración dinámica**: Genera descripciones y eventos únicos adaptados a las decisiones de los jugadores.
- **Gestión de encuentros**: Crea y administra combates y situaciones de forma automatizada.
- **Interfaz intuitiva**: Diseñada con Streamlit para una experiencia de usuario sencilla y accesible.
- **Personalización**: Ajusta parámetros para adaptar la aventura a tu estilo de juego.

## 🧰 Tecnologías utilizadas

- [OpenAI API](https://openai.com/api/): Para la generación de texto y eventos.
- [Streamlit](https://streamlit.io/): Framework para la creación de la interfaz web.
- [Python 3](https://www.python.org/): Lenguaje de programación principal del proyecto.

## 📦 Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/borjabarber/Dungeon_Master.git
   cd Dungeon_Master
   ```

2. **Crea y activa un entorno virtual (opcional pero recomendado):**

   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

3. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configura tu clave de API de OpenAI:**

   Asegúrate de tener una clave válida de OpenAI y configúrala en tu entorno como una variable de entorno:

   ```bash
   export OPENAI_API_KEY='tu_clave_aquí'  # En Windows: set OPENAI_API_KEY=tu_clave_aquí
   ```

5. **Ejecuta la aplicación:**

   ```bash
   streamlit run app.py
   ```

## 📁 Estructura del proyecto

```
Dungeon_Master/
├── images/           # Imágenes utilizadas
├── src/              # Código fuente principal
├── video/            # Video Demo de la App 
├── app.py            # Archivo principal de la aplicación Streamlit
├── requirements.txt  # Lista de dependencias
├── README.md         # Este archivo
└── LICENSE           # Licencia del proyecto
```

## 📹 Demostración

[Ver video de demostración](https://vimeo.com/1083470886)


## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar la aplicación, solucionar errores o agregar nuevas funciones, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama: `git checkout -b nombre-de-la-rama`.
3. Realiza tus cambios y haz commit: `git commit -m 'Descripción de los cambios'`.
4. Sube tu rama: `git push origin nombre-de-la-rama`.
5. Abre un Pull Request.

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más información.
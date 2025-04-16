# Changelog

---

### Día 1 – `v1.0-day1`  

**Commit:** Configuración inicial y Dockerfiles

- Se creó un `.gitignore` para proyectos en Python.  
- Se creó un `Dockerfile` para la imagen del juego de la  trivia.  
- Se creó un `docker-compose.yml` para levantar los servicios: app (trivia) y base de datos (PostgreSQL).

---

### Día 2 – `v1.0-day2`  

**Commit:** Implementación inicial de lógica y pruebas  

- Se creó el archivo `test_trivia.py` para pruebas unitarias.  
- Se creó el archivo `trivia.py` con la clase `Question`.

---

### Día 3 – `v1.0-day3`  

 **Commit:** Implementación de la Clase `Quiz` y flujo básico del juego  

- Se implementó la clase `Quiz` con los métodos:  
  - `add_questions`: agrega una nueva pregunta
  - `get_next_question`: retorna la siguiente pregunta de la lista de preguntas  
  - `run_quiz`: toma cada pregunta de la lista de preguntas, y muestra por la consola su lista de alternativas, espera que el usuario ingrese la alternativa para indicarle si la respuesta es correcta o no

---

### Día 4 – `v1.0-day4`  

**Commit:** Implementación del sistema de puntuación, manejo de rondas y finalización del juego  

- Se creó el archivo `main.py` para probar `Quiz`.  
- Se corrigió un error en `test_trivia.py`.  
- Se agregaron atributos `correct_answers` e `incorrect_answers`.  
- Se agregó feedback al usuario sobre su puntaje (preguntas acertadas, puntuación general).  
- Se creó el método `answer_question`.

---

### Día 5 – `v1.0-day5`

**Commit:** Mejoro la interfaz del usuario pero también agrego la conexión con la base de datos y mejoras en la UI  

- Se usó `psycopg2`para la conexión con postgres.  
- Se incorporó acceso a variables de entorno mediante `env_file` en los contenedores.  
- Se mejoró la interfaz: mensaje de bienvenida, instrucciones y niveles.  
- Se agregó lógica para obtener preguntas desde la base de datos según el nivel.

**Commit:** Creo Script para crear la tabla e insertar las preguntas en la base de datos

- Se creó `datos.sql` con la estructura de tabla `preguntas`.  
- Se incluyeron 30 preguntas distribuidas en 3 niveles (10 por nivel).

**Commit:** Actualizo el docker y requirements.txt para la conexión con la base de datos

- Se actualizó `docker-compose.yml` para que `app` espere a que inicie `postgres`.  
- Se agregó psycopg2-binary a requirements.txt.

---

### Día 6 – `v1.0-day6`

**Commit:** Añado la condición de service_healthy a docker-compose  

- Se agregó `env_file` al servicio `app` para tener una estructura más limpia.  
- Se usó `service_healthy` en postgres para asegurar que esté listo antes de ejecutar app.  
- Se cambió `fastapi` a fastapi[all] y se eliminó uvicorn de `requirements.txt`.

**Commit:** Creo un archivo para la conexión con la bd y modifico las importaciones  

- Se creó `db.py` que se encargará exclusivamente de crear la conexión con la base de datos.  
- Se actualizaron las importaciones.

**Commit:** Agrego el endpoint POST `/questions/`  que inserta preguntas en la base de datos

- Se creó el endpoint para insertar preguntas en la base de datos,si todo sale bien retorna un 200 y si no 500.

**Commit:** Configuración de pipeline CI/CD y pruebas de integración

- Se creó `.github/workflows/ci.yml` , el cual automatiza las integraciones.  
- Se creó test_api.py para probar los endpoints (por ahora solo POST /questions/create).

---

### Día 7 – `v1.0-day7`

**Commit:** Agrego nuevos test

- Se modificó el endpoint de creación y se actualizó en los tests.  
- Se agregaron pruebas para buscar pregunta por ID y para verificar el correcto guardado en la base de datos mediante `data.json`, que almacena todas las preguntas.

**Commit:** Agrego todo el directorio en el docker y agrego envfile al docker compose

- Se copió todo el proyecto (la ruta raiz ya no solo `app/`) en el contenedor.  
- `Postgres`(contenedor) ahora también usa `env_file`.

**Commit:** Agrego locust y bandit en requirements

- Se agregaron locust y bandit a `requirements.txt`.

**Commit:** Formateo los archivos *.py

- Se aplicó formato a los archivos .py con flake8.

**Commit:** Actualizo el ci.yml para bandit

- Se agregó paso de escaneo de seguridad al pipeline.
  
**Commit:** Agrego el archivo `locustfile.py`

- Se creó `locustfile`.py para el endpoint `/questions/create`.
  
**Commit:** Agrego endpoints questions/create , questions/id y questions

- Se renombró `/questions/` a `/questions/create`.  
- Se agregaron:  
  - `GET /questions/{id}`: retorna la pregunta mediante el id  
  - `GET /questions`: retorna todas las preguntas

**Commit:** Preguntas en archivo json

- Se creó `data.json` que almacena todas las preguntas para el test.

**Commit:** Corregí la ubicación del ci.yml

- Se renombró el archivo `github/workflows/ci.yml` a `.github/workflows/ci.yml`.

**Commit:** Agrego dotenv

- Se agregó `dotenv` para manejar variables de entorno.

**Commit:** Modifico el ci.yml para iniciar el servicio de postgres

- Se configuró `ci.yml` para levantar el servicio de base de datos.

**Commit:** Fix : path para el env y url para el sonar

- Se corrigió ruta de `load_dotenv`.  
- Se agregó `SONAR_HOST_URL` como variable de entorno.

---

### Observaciones

- El test con `pytest` no se ejecuta correctamente en GitHub Actions, pero en el local(uso de docker) funciona correctamente.
- Se intentó ajustar la configuración del pipeline, sin éxito hasta el momento.  
- Se identificó un problema con la versión de Java al ejecutar Sonar, persiste incluso tras actualizarla.  
- Se retrasó la entrega del proyecto debido a la insistencia de resolver estos errores .

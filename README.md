Proyecto Gobierno de datos y analitica

Requisitos
- Python instalado.
- Acceso a una base de datos PostgreSQL.

Dependencias
Las dependencias necesarias están listadas en el archivo `requirements.txt` Estas incluyen:
- pandas: para manipulación de archivos Parquet.
- sqlalchemy: para interactuar con PostgreSQL.
- psycopg2: controlador PostgreSQL.
- azure-storage-blob: para acceder a Azure Blob Storage.
- Pillow: para manejar imágenes en la GUI.
- tkinter: para la interfaz gráfica.

Paso 1: Clonar el repositorio desde GitHub
Tener Python instalado

Paso 2: Instalar las dependencias
Instalar las dependencias.

Paso 3: Configuración de la Carpeta de Descargas
El proyecto utiliza una carpeta llamada Downloads dentro del repositorio para almacenar los archivos Parquet que se descargan de Azure Blob Storage.

Paso 4: Ejecutar la Aplicación
ejecuta el archivo app.py para iniciar la aplicación.
La aplicación abrirá una interfaz gráfica donde se debera ingresar los siguientes datos:
Azure Account URL: La URL de tu cuenta de Azure Blob Storage.
Container Name: El nombre del contenedor en Azure Blob Storage que contiene los archivos Parquet.
SAS Token: El token de acceso compartido (SAS) para acceder a Azure Blob Storage.
PostgreSQL Connection URL: La URL de conexión a la base de datos PostgreSQL, en el formato: postgresql://postgres:mi_contraseña@localhost:5432/mi_base_datos
Una vez ingresados los datos, presiona el botón "Actualizar Datos" para descargar los archivos Parquet de Azure y subir los datos a PostgreSQL.

Paso 5: crear la relacion entre las tablas si estas no existen PK Y FK.
- ALTER TABLE "Jobs" ADD CONSTRAINT "pk_jobs" PRIMARY KEY ("job-id");
- ALTER TABLE "Job_Applications" ADD CONSTRAINT fk_job_applications_job_id FOREIGN KEY ("job-id") REFERENCES "Jobs"("job-id");
al abrir el archivo de Power Bi automaticamente toma la relacion por lo que ya esta predeterminado.

Paso 6: visualizacion
abrir el archivo de visualizacion (Seleccion de Candidatos.pbix) y hacer las respectivas conexion con la base de datos PostgresSQL

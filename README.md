Proyecto Gobierno de datos y analitica

Requisitos
- Python instalado.
- Acceso a una base de datos PostgreSQL.
- Power Bi instalado.

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

Paso 2: Instalar las dependencias.

Paso 3: Configuración de la Carpeta de Descargas
El proyecto utiliza una carpeta llamada Downloads dentro del repositorio para almacenar los archivos Parquet que se descargan de Azure Blob Storage.

Paso 4: Ejecutar la Aplicación
ejecuta el archivo azure_blob_to_postgres_updater.py para iniciar la aplicación.
La aplicación abrirá una interfaz gráfica donde se debera ingresar los siguientes datos:
Azure Account URL: La URL de Azure Blob Storage.
Container Name: nombre del contenedor en Azure Blob Storage que contiene los archivos.
SAS Token: token de acceso compartido (SAS) para acceder a Azure Blob Storage.
PostgreSQL Connection URL: La URL de conexión a la base de datos PostgreSQL, en el formato: postgresql://postgres:mi_contraseña@localhost:5432/mi_base_datos
Una vez ingresados los datos, presiona el botón "Actualizar Datos" para descargar los archivos Parquet de Azure y subir los datos a PostgreSQL.

Paso 5: crear la relacion entre las tablas si estas no existen PK Y FK.                                
Al abrir el archivo de Power Bi automaticamente toma la relacion por lo que ya esta predeterminado en las pruebas.

Paso 6: visualizacion
Seleccionar el boton abrir Power Bi para abrir automaticamente el archivo (Seleccion de Candidatos.pbix) y hacer las respectivas conexion con la base de datos PostgreSQL aunque estas ya vienen predefinidas.

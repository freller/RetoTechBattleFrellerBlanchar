import os
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from azure.storage.blob import ContainerClient
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime

parquet_directory = os.path.join(os.path.dirname(__file__), 'Downloads')

pbix_file_path = os.path.join(os.path.dirname(__file__), 'Visualizacion', 'Seleccion de Candidatos.pbix')

def get_psycopg2_connection(postgres_url):
    return psycopg2.connect(postgres_url)


def download_blobs(account_url, container_name, sas_token, parquet_directory):
    container_client = ContainerClient(account_url=account_url, container_name=container_name, credential=sas_token)
    blobs_list = container_client.list_blobs()


    if not os.path.exists(parquet_directory):
        os.makedirs(parquet_directory)											   

    for blob in blobs_list:
        blob_client = container_client.get_blob_client(blob)
        download_path = os.path.join(parquet_directory, blob.name)
        if not os.path.exists(download_path):  
            print(f"Descargando {blob.name}...")
            with open(download_path, "wb") as file:
                download_stream = blob_client.download_blob()
                file.write(download_stream.readall())
            print(f"Archivo {blob.name} descargado en {download_path}")


def process_parquet_files(parquet_directory, engine):
    if not os.path.exists(parquet_directory):
        raise FileNotFoundError(f"El directorio '{parquet_directory}' no existe.")

    for filename in os.listdir(parquet_directory):
        if filename.endswith('.parquet'):
            parquet_file = os.path.join(parquet_directory, filename)
            table_name = os.path.splitext(filename)[0]

            try:
                df = pd.read_parquet(parquet_file)
                print(f"Archivo Parquet '{filename}' leído exitosamente.")
                df.to_sql(table_name, engine, if_exists='replace', index=False)
                print(f"Datos importados exitosamente a la tabla '{table_name}'.")
            except Exception as e:
                print(f"Error al procesar el archivo '{filename}': {e}")


def actualizar_datos():
    azure_account_url = azure_account_entry.get()
    azure_container_name = azure_container_entry.get()
    azure_sas_token = azure_sas_token_entry.get()
    postgres_url = postgres_entry.get()

    engine = create_engine(postgres_url)
    
    download_blobs(azure_account_url, azure_container_name, azure_sas_token, parquet_directory)
    process_parquet_files(parquet_directory, engine)
    
    last_update_time.set(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    messagebox.showinfo("Actualización Completa", "Los datos se han actualizado correctamente.")

def abrir_power_bi():

    if os.path.exists(pbix_file_path):
        os.startfile(pbix_file_path)
    else:
        messagebox.showerror("Error", f"El archivo '{pbix_file_path}' Power Bi no existe.")

root = tk.Tk()
root.title("Actualizador de Datos")

image_path = os.path.join(os.path.dirname(__file__), 'imagen', 'Definit.png')
bg_image = Image.open(image_path)
bg_photo = ImageTk.PhotoImage(bg_image)

root.geometry(f"{bg_image.width}x{bg_image.height}")

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

azure_frame = tk.Frame(root, bg='white', bd=5)
azure_frame.place(relx=0.5, rely=0.20, relwidth=0.70, relheight=0.25, anchor='n')

tk.Label(azure_frame, text="Azure Account URL:").grid(row=0, column=0, sticky='w')
azure_account_entry = tk.Entry(azure_frame)
azure_account_entry.grid(row=0, column=1)

tk.Label(azure_frame, text="Container Name:").grid(row=1, column=0, sticky='w')
azure_container_entry = tk.Entry(azure_frame)
azure_container_entry.grid(row=1, column=1)

tk.Label(azure_frame, text="SAS Token:").grid(row=2, column=0, sticky='w')
azure_sas_token_entry = tk.Entry(azure_frame)
azure_sas_token_entry.grid(row=2, column=1)

postgres_frame = tk.Frame(root, bg='white', bd=5)
postgres_frame.place(relx=0.5, rely=0.35, relwidth=0.70, relheight=0.07, anchor='n')

tk.Label(postgres_frame, text="PostgreSQL Conexion URL:").grid(row=0, column=0, sticky='w')
postgres_entry = tk.Entry(postgres_frame)
postgres_entry.grid(row=0, column=1)

update_button = tk.Button(root, text="Actualizar Datos", command=actualizar_datos, font=("Helvetica", 16))
update_button.place(relx=0.5, rely=0.47, anchor='n')

open_pbix_button = tk.Button(root, text="Abrir visualizacion", command=abrir_power_bi, font=("Helvetica", 12))
open_pbix_button.place(relx=0.5, rely=0.75, anchor='n')

last_update_time = tk.StringVar()
tk.Label(root, text="Última actualización:", font=("Helvetica", 12)).place(relx=0.5, rely=0.56, anchor='n')
tk.Label(root, textvariable=last_update_time, font=("Helvetica", 12)).place(relx=0.5, rely=0.60, anchor='n')														

root.mainloop()


import mysql.connector
import os
import streamlit as st

# Obtener las credenciales de las variables de entorno (seguridad)
host = os.getenv("DB_HOST", "bhmjgn6rddt8wzxjsi17-mysql.services.clever-cloud.com")
user = os.getenv("DB_USER", "uibfqsmgnn6lvxje")
password = os.getenv("DB_PASSWORD", "plNHPej2eacLK4vHSSZn")
database = os.getenv("DB_NAME", "bhmjgn6rddt8wzxjsi17")

# Intentar establecer la conexión
try:
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    
    # Verificar si la conexión fue exitosa
    if conn.is_connected():
        st.success("Conexión exitosa a la base de datos MySQL.")
    else:
        st.error("No se pudo conectar a la base de datos.")
        
except mysql.connector.Error as err:
    # Mostrar el error si la conexión falla
    st.error(f"Error al conectar con la base de datos: {err}")

finally:
    if conn.is_connected():
        # Cerrar la conexión
        conn.close()

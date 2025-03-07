import boto3
import requests
import datetime

def scrape_mitula(event, context):
    print("Ejecutando scrape_mitula...")

    base_url = "https://casas.mitula.com.co/find?operationType=sell&propertyType=mitula_studio_apartment&geoId=mitula-CO-poblacion-0000014156&text=Bogot%C3%A1%2C++%28Cundinamarca%29"
    fecha_hoy = datetime.datetime.now().strftime("%Y-%m-%d")
    s3 = boto3.client('s3')
    bucket_name = "landing-casas-059"  # Cambia según tu bucket

    for page in range(1, 11):
        url = f"{base_url}?p={page}"
        response = requests.get(url)

        if response.status_code == 200:
            file_name = f"{fecha_hoy}-p{page}.html"
            file_path = f"/tmp/{file_name}"

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(response.text)

            s3.upload_file(file_path, bucket_name, f"{fecha_hoy}/{file_name}")
            print(f"Página {page} guardada en {bucket_name}/{fecha_hoy}/{file_name}")
        else:
            print(f"Error al descargar página {page}, código: {response.status_code}")

    return {"status": "OK"}

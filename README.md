# Weather Agent on Cloud Run

Práctica creando un agente sencillo de consulta sobre el clima en distintas ciudades del mundo desplegado en la nube GCP con Cloud Run y ADK.

## Despliegue

1. Se crea una carpeta local donde se colocan los archivos, de estructura básica del agente, __init__.py y agent.py.

   Se utiliza la siguiente estructura:

- [__init__.py](https://github.com/MatiasMaxRodriguez/Agent_on_Cloud_Run/blob/main/__init__.py)
- [agent.py](https://github.com/MatiasMaxRodriguez/Agent_on_Cloud_Run/blob/main/agent.py)

2. En la terminal, realizar login a la cuenta de GCP con el comando: gcloud auth login.

3. Crear un nuevo proyecto. Este se puede realizar a través de terminal o en la consola GCP.

4. Habilitar la facturación del proyecto.

5. Antes de hacer el deploy del agente con ADK, tener en cuenta de dar todos los permisos de IAM y habilitar todas las APIS correspondientes. Los permisos de IAM se aplican a la Service Account con los siguientes roles:

   --role="roles/cloudbuild.builds.builder"

   --role="roles/storage.admin"

   --role="roles/artifactregistry.writer"

   --role="roles/aiplatform.user"

   APIs a habilitar desde terminal:

   gcloud services enable aiplatform.googleapis.com (Habilita API de Vertex AI)

   gcloud services enable run.googleapis.com (Habilita la API de Cloud Run)

6. Realizar el deploy con ADK utilizando desde la terminal el siguiente comando:
   ```
   adk deploy cloud_run \
       --project=nombre_del_proyecto \
       --region=region_del_proyecto \
       --service_name=nombre_del_agente \
       --with_ui \
       /path_local/al/agente
   ```

## Tecnologías utilizadas:

[Agent Development Kit (ADK)](https://adk.dev/),
[Python](https://www.python.org/),
[Cloud Run](https://cloud.google.com/run?hl=es),
[GCP](https://cloud.google.com/)

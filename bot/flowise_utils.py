import os
import config
from datetime import datetime
import requests

PINECONE_API_KEY = config.pinecone_api_key
PINECONE_ENV = config.pinecone_env
PINECONE_INDEX = config.pinecone_index_name
os.environ['OPENAI_API_KEY'] = config.openai_api_key

def upsert_txt_document(document_path: str, namespace: str, user_id: int):
    API_URL = "https://8783-175-143-213-159.ngrok-free.app/api/v1/prediction/d7a7691a-e216-492c-ac2e-62c9a6cba98e"
    # use form data to upload files
    form_data = {
        "files": (document_path, open(document_path, 'rb'))
    }
    values = {
        "pineconeEnv": PINECONE_ENV,
        "pineconeIndex": PINECONE_INDEX,
        "pineconeNamespace": get_user_namespace(namespace, user_id),
        "question": "Summarize the document in one sentence."
    }
    response = requests.post(API_URL, files=form_data, data=values)
    
    return response.text

def upsert_pdf_document(document_path: str, namespace: str, user_id: int):
    API_URL = "https://8783-175-143-213-159.ngrok-free.app/api/v1/prediction/5df81587-f80c-42b2-b6c9-8f3ca67950fb"
    # use form data to upload files
    form_data = {
        "files": (document_path, open(document_path, 'rb'))
    }
    values = {
        "pineconeEnv": PINECONE_ENV,
        "pineconeIndex": PINECONE_INDEX,
        "pineconeNamespace": get_user_namespace(namespace, user_id),
        "question": "Summarize the document in one sentence."
    }
    response = requests.post(API_URL, files=form_data, data=values)

    return response.text

def query(message: str, namespace: str, user_id: int):
    API_URL = "https://8783-175-143-213-159.ngrok-free.app/api/v1/prediction/d306eda3-d8db-417a-87d5-217919c6103f"
    # use form data to upload files
    payload = {
        "question": message,
        "overrideConfig": {
            "pineconeEnv": PINECONE_ENV,
            "pineconeIndex": PINECONE_INDEX,
            "pineconeNamespace": get_user_namespace(namespace, user_id)
            }
    }
    response = requests.post(API_URL, json=payload)

    return response.text

def get_user_namespace(namespace: str, user_id: int):
    return str(user_id) + "_" + namespace
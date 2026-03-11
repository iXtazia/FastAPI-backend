from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

from app.core.config import MONGO_URI, DB_NAME

client = MongoClient(
    MONGO_URI,
    server_api=ServerApi("1"),
    tls=True,
    tlsCAFile=certifi.where()
)

try:
    client.admin.command("ping")
    print("Connected successfully!")
except Exception as e:
    print("Error:", e)

db = client[DB_NAME]
import psycopg2
from common.config import DB_CONFIG

conn = psycopg2.connect(**DB_CONFIG)
print("Connexion OK")
conn.close()
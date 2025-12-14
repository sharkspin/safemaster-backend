import os

import psycopg2
from dotenv import load_dotenv

# Load variables from a local .env so secrets are not hard-coded.
load_dotenv()

# Prefer a full connection string (recommended for Supabase) to avoid
# URL-encoding issues with special characters in passwords.
DB_URL = os.getenv("SUPABASE_DB_URL")

# Fallback to discrete settings if a single URL isn't provided.
DB_CONFIG = {
    "user": os.getenv("SUPABASE_DB_USER"),
    "password": os.getenv("SUPABASE_DB_PASSWORD"),
    "host": os.getenv("SUPABASE_DB_HOST"),
    "port": os.getenv("SUPABASE_DB_PORT", "5432"),
    "dbname": os.getenv("SUPABASE_DB_NAME"),
}


def get_db():
    if DB_URL:
        return psycopg2.connect(DB_URL)

    if all(DB_CONFIG.values()):
        return psycopg2.connect(**DB_CONFIG)

    raise RuntimeError(
        "Database credentials are missing. Set SUPABASE_DB_URL or individual SUPABASE_DB_* vars."
    )

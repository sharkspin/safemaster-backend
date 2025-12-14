import psycopg2


DB_URL = "postgresql://postgres:.QSUzFV6Fa7_-#q@db.dfrkmbswctmvlkiwluvo.supabase.co:5432/postgres"


def get_db():
    # Use provided connection string for hosted Postgres instance.
    return psycopg2.connect(DB_URL)

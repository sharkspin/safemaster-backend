import psycopg2


DB_URL = (
    "postgresql://userdb_h15g_user:kE8SFJpUfjbnUo0LvvMoIaop0G6kUyvW@"
    "dpg-d4vb93be5dus73ab4scg-a/userdb_h15g"
)


def get_db():
    # Use provided connection string for hosted Postgres instance.
    return psycopg2.connect(DB_URL)

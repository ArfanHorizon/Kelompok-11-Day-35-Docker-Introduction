import psycopg2

# Connect to source and destination databases
source_conn = psycopg2.connect(
    dbname="source_db",
    user="postgres",
    password="hajiku1234soa",
    host="localhost",  # Service name in Docker Compose
    port="5432"
)

destination_conn = psycopg2.connect(
    dbname="target",
    user="postgres",
    password="hajiku1234soa",
    host="localhost",  # Service name in Docker Compose
    port="5432"
)

# ETL function


def perform_etl():
    try:
        # Extract data from source table
        with source_conn.cursor() as source_cur:
            source_cur.execute("SELECT * FROM source_table")
            rows = source_cur.fetchall()

        # Transform data if needed

        # Load data into destination table
        with destination_conn.cursor() as destination_cur:
            for row in rows:
                # Assuming destination table has same schema as source table
                destination_cur.execute(
                    "INSERT INTO source_table VALUES (%s, %s, %s)", row)

        destination_conn.commit()
        print("ETL process completed successfully.")
    except psycopg2.Error as e:
        print("Error during ETL process:", e)
    finally:
        source_conn.close()
        destination_conn.close()


if __name__ == "__main__":
    perform_etl()

from db.connection import create_connection


def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS postal_codes (
            post_code VARCHAR(20) PRIMARY KEY,
            country VARCHAR(100),
            longitude FLOAT,
            latitude FLOAT,
            state VARCHAR(100)
        );
    ''')

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    create_tables()

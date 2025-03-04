from sqlalchemy.orm import sessionmaker

from db.connection import create_connection, get_engine
from db.models import PostalCode


class PostalCodeRepository:
    @staticmethod
    def get_postal_info_psycopg2(post_code):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM postal_codes WHERE post_code = %s', (post_code,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return PostalCode(post_code=result[0], country=result[1], longitude=result[2], latitude=result[3],
                              state=result[4])
        return None

    @staticmethod
    def save_postal_info_psycopg2(postal_code):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO postal_codes (post_code, country, longitude, latitude, state)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (post_code) DO NOTHING
        ''', (postal_code.post_code,
              postal_code.country,
              postal_code.longitude,
              postal_code.latitude,
              postal_code.state))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_postal_info_sqlalchemy(post_code):
        engine = get_engine()
        session = sessionmaker(bind=engine)()
        return session.query(PostalCode).filter_by(post_code=post_code).first()

    @staticmethod
    def save_postal_info_sqlalchemy(postal_code):
        engine = get_engine()
        session = sessionmaker(bind=engine)()
        session.add(postal_code)
        session.commit()

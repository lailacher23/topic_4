from services.postal_service_psycopg2 import PostalServicePsycopg2
from services.postal_service_sqlalchemy import PostalServiceSQLAlchemy


def main():
    post_code = input("Введите почтовый индекс: ")
    # Использование подхода psycopg2
    info_psycopg2 = PostalServicePsycopg2.get_postal_info(post_code)
    if info_psycopg2:
        print(
            f"[psycopg2] Долгота: {info_psycopg2.longitude}, Широта: {info_psycopg2.latitude}, "
            f"Страна: {info_psycopg2.country}, Субъект: {info_psycopg2.state}")
    else:
        print("[psycopg2] Почтовый индекс не найден.")

    # Использование подхода SQLAlchemy
    info_sqlalchemy = PostalServiceSQLAlchemy.get_postal_info(post_code)
    if info_sqlalchemy:
        print(
            f"[SQLAlchemy] Долгота: {info_sqlalchemy.longitude}, Широта: {info_sqlalchemy.latitude}, "
            f"Страна: {info_sqlalchemy.country}, Субъект: {info_sqlalchemy.state}")
    else:
        print("[SQLAlchemy] Почтовый индекс не найден.")


if __name__ == "__main__":
    main()

import requests

from db.models import PostalCode
from db.repository import PostalCodeRepository


class PostalServicePsycopg2:
    @staticmethod
    def get_postal_info(post_code):
        postal_code = PostalCodeRepository.get_postal_info_psycopg2(post_code)
        if not postal_code:
            postal_code = PostalServicePsycopg2.get_postal_info_from_api(post_code)
            if postal_code:
                PostalCodeRepository.save_postal_info_psycopg2(postal_code)
        return postal_code

    @staticmethod
    def get_postal_info_from_api(post_code):
        response = requests.get(f'https://api.zippopotam.us/RU/{post_code}')
        if response.status_code == 200:
            data = response.json()
            place = data['places'][0]
            return PostalCode(
                post_code=data['post code'],
                country=data['country'],
                longitude=float(place['longitude']),
                latitude=float(place['latitude']),
                state=place['state']
            )
        return None

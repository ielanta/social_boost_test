import requests

from social_boost_test.settings import HUNTER_IO_API_KEY, HUNTER_IO_URL
URL = 'https://api.hunter.io/v2/email-verifier'


def verify_email(email):
    data = {'email': email, 'api_key': HUNTER_IO_API_KEY}
    result = requests.get(HUNTER_IO_URL, params=data)
    if result.status_code != 200:
        return result.json()
    return result.json()['data']

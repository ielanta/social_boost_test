import clearbit

from social_boost_test.settings import CLEARBIT_API_KEY


def get_clearbit_data(email):
    clearbit.key = CLEARBIT_API_KEY
    person = clearbit.Person.find(email=str(email))
    if person:
        return format_data(dict(person))


def format_data(person):
    return {
        'name': person['name']['fullName'] if person.get('name') else '',
        'location': person.get('location'),
        'bio': person.get('bio'),
        'site': person.get('site'),
        'employment': person['employment']['title'] if person.get('employment') else '',
        'company_role': person['employment']['role'] if person.get('employment') else '',
        'seniority': person['employment']['seniority'] if person.get('employment') else '',
        'facebook': person['facebook']['handle'] if person.get('facebook') else '',
        'github': person['github']['handle'] if person.get('github') else '',
        'twitter': person['twitter']['handle'] if person.get('twitter') else '',
        'linkedin': person['linkedin']['handle'] if person.get('linkedin') else '',
    }

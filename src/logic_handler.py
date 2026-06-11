import json
from country import Country

def load_country_file(country_file):
    with open(country_file) as f:
        country_dict = json.load(f)
    return country_dict


def load_countries(country_dict):
    countries = []
    for country in country_dict:
        cca3= country['cca3']
        country_name= country['translations']['deu']['common']
        languages_data = country['languages']
        if isinstance(languages_data, dict):
            languages = list(languages_data.values())
        else:
            languages = list(languages_data)
        capital = country['capital']
        border = country['borders']
        population = country['population']
        continents  = country['continents']
        countries.append(Country(country_name, cca3, capital, border, languages, population, continents))


    return countries

import os.path

import flet as ft
from flet import View, Text, Row, View, Page, AppBar, Button, Text, IconButton, Image
from logic_handler import load_country_file, load_countries
from country import Country
import random

#TODO check countries with no flag image


def init_app():
    json_loaded = load_country_file('src/countries.json')

    return load_countries(json_loaded)


def get_random_country(countries_loaded: list[Country]):
    random__int = random.randrange(len(countries_loaded)-1)
    return countries_loaded.pop(random__int)






def main(page: ft.Page):
    countries_loaded: list[Country] = init_app()
    random_country = get_random_country(countries_loaded)


    def start_game(e):
        print("Game started")

    def next_country(e):
        next_country_ = get_random_country(countries_loaded)
        flag_image.src = next_country_.country_code + '.png'
        text_field_country_name.value = next_country_.country_name
        text_field_capital_city.value = next_country_.capital_city
        text_field_population.value = next_country_.population
        text_field_continent.value = next_country_.continent
        page.update()

    flag_image = Image(width=600, height=200, repeat=ft.ImageRepeat.NO_REPEAT, src=random_country.country_code + '.png')
    text_field_country_name = Text(value=f'Name {random_country.country_name}', size=30)
    text_field_capital_city = Text(value=str(random_country.capital_city), size=30)
    text_field_population = Text(value=str(random_country.population), size=30)
    text_field_continent= Text(value=str(random_country.continent), size=30)

    page.views.append(View(route="/", controls=[

        flag_image,
        text_field_country_name,
        text_field_capital_city,
        text_field_population,
        text_field_continent,
        Button(text="next country", on_click=next_country),
        Button(text="Continent Guess", on_click=start_game, icon=ft.Icons.ALARM),]))

    page.update()
if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")

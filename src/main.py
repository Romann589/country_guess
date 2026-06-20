import os.path
from unidecode import unidecode
import flet as ft
from flet import View, Text, Row, View, Page, AppBar, Button, Text, IconButton, Image, TextField, Column, MainAxisAlignment, CrossAxisAlignment, Window
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

def generate_x(next_country_name: str) -> str:
    hidden_name = ""

    for char in next_country_name:
        if char in [" ", "/", "-"]:
            hidden_name += char
        else:
            hidden_name += "*"

    return hidden_name



def main(page: ft.Page):
    background_music = ft.Audio(
        src="sounds/Background_music.mp3",
        autoplay=True,
        volume=0.3,
        release_mode=ft.audio.ReleaseMode.LOOP,
    )
    page.overlay.append(background_music)

    flag_image = Image(width=600, height=200, repeat=ft.ImageRepeat.NO_REPEAT)
    text_field_country_name = Text(value="", size=30)
    text_field_capital_city = Text(value=str(), size=30)
    text_field_languages = Text(value=str(), size=30)
    text_field_continent= Text(value=str(), size=30)
    text_field_population = Text(value=str(), size=30)
    guess_text_field = TextField(label="", width=500)
    current_country_name = str()
    hints_remaining_text_field = Text(value=str(), size=30)
    score_counter_text_field = Text(value=str(), size=30)
    countries_loaded: list[Country] = init_app()
    score_counter = 0
    hints_remaining = 4

    def start_game(e):
        print("Game started")
    
    music_is_playing = True

    def music(e):
        nonlocal music_is_playing

        if music_is_playing:
            background_music.pause()
            music_is_playing = False
        else:
            background_music.play()
            music_is_playing = True
    
    def close_game(e):
        page.window.destroy()

    def check_guess(e):
        nonlocal hints_remaining, score_counter
        answer = unidecode(str(guess_text_field.value))
        print(answer)
        correct_answer = unidecode(current_country_name)
        if hints_remaining == 0:
            next_country(e)
        elif str(answer).lower() == correct_answer.lower():
            score_counter += 1 + hints_remaining
            score_counter_text_field.value = f"Score: {score_counter}"
            next_country(e)
        else:
            give_hint()
            hints_remaining -= 1
            hints_remaining_text_field.value = f"Hints remaining: {hints_remaining}"
        page.update()
    
    def give_hint():
        if hints_remaining == 4:
            guess_text_field.label = f"💡: Der Kontinent ist {str(text_field_continent.value).strip('[]')}"
        elif hints_remaining == 3:
            guess_text_field.label = f"💡: Die Hauptstadt ist {str(text_field_capital_city.value).strip('[]')}"
        elif hints_remaining == 2:
            guess_text_field.label = f"💡: Die Sprache ist {text_field_languages.value}"
        elif hints_remaining == 1:
            guess_text_field.label = f"💡: Der Ländername beginnt mit {current_country_name[0]}"

    def next_country(e):
        nonlocal current_country_name, hints_remaining
        next_country_: Country= get_random_country(countries_loaded)
        hints_remaining = 4
        hints_remaining_text_field.value = f"Hints remaining: {hints_remaining}"
        current_country_name = next_country_.country_name.lower().replace("name ", "")
        flag_image.src = next_country_.country_code + '.png'
        text_field_country_name.value = next_country_.country_name
        text_field_capital_city.value = str(next_country_.capital_city)
        text_field_continent.value = str(next_country_.continent)
        text_field_population.value = str(next_country_.population)
        text_field_languages.value = ", ".join(next_country_.languages)
        guess_text_field.label = generate_x(next_country_.country_name)
        page.update()
    next_country(None)
    page.views.append(View(route="/", controls=[

        AppBar(title=Text("Home"), actions=[score_counter_text_field, hints_remaining_text_field]),
        flag_image,
        guess_text_field,
     #   text_field_country_name,
        Row(controls=[
        Button(text="next country", on_click=next_country),
        Button(text="check guess", on_click=check_guess),
        Button(text="Close App", on_click=close_game),
        Button(text="Music On / Off", on_click=music),
        ],alignment=MainAxisAlignment.CENTER),],
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=26
        
        
        ))

    page.update()
    background_music.play()
if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")

import requests
import json
import os

country_file = open("countries.json")
countries = json.load(country_file)


for country in countries:
    flag_url = country['flags']['png']
    file_name = country['cca3']

    response_ = requests.get(flag_url)
    if response_.status_code == 200:
        with open(os.path.join("src", "assets", (file_name + ".png")), "wb") as file:
            file.write(response_.content)
            print(file_name + ".png")









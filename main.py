import turtle
import pandas as pd
from text_write import TextOnMap

screen = turtle.Screen()
screen.title("Arab Countries Game")
img = "arab_map.gif"
screen.addshape(img)
turtle.shape(img)

text = TextOnMap()
lang_prompt = screen.textinput(title="Language/اللغة",prompt="Enter 'english' for english language\nاكتب 'العربية' للغة العربية ").lower()

if lang_prompt == "english":  # English
    answer = screen.textinput(title="Country Name", prompt="Enter a country name\nWrite 'Exit' to quit").title()

    data = pd.read_csv('c_en.csv')
    country_list = data["country"].to_list()
    print(country_list)
    inserted_countries = []
    while answer != "Exit":
        if answer in country_list:
            country_info = data[data.country == answer]
            text.write_name(name=answer, x_position=country_info.x, y_position=country_info.y)
            inserted_countries.append(answer)
        answer = screen.textinput(title=f"{len(inserted_countries)}/22 country", prompt="Enter a country name").title()

        if len(inserted_countries) >= 22:
            break


else:  # Arabic
    answer = screen.textinput(title="اسم الدولة", prompt="اكتب اسم دولة\nاكتب 'خروج' لمغادرة البرنامج").title()

    data = pd.read_csv('c_ar.csv')
    country_list = data["country"].to_list()
    inserted_countries = []

    while answer != "خروج":
        if answer in country_list:
            country_info = data[data.country == answer]
            text.write_name(name=answer, x_position=country_info.x, y_position=country_info.y)
            inserted_countries.append(answer)
            answer = screen.textinput(title=f"{len(inserted_countries)}/22 country", prompt="Enter a country name").title()

        if len(inserted_countries) >= 22:
            break

if len(inserted_countries) < 22:
    countries_missed = list(set(country_list) - set(inserted_countries))
    pd.DataFrame(countries_missed).to_csv("missed countries.csv")







import turtle
import pandas as pd
from text_write import TextOnMap

# Screen setup
screen = turtle.Screen()
screen.title("Arab Countries Game")
img = "arab_map.gif"  # importing image
screen.addshape(img)
turtle.shape(img)

text = TextOnMap()  # making an object to write on screen
# choose language
lang_prompt = screen.textinput(title="Language/اللغة",prompt="Enter 'english' for english language\nاكتب 'العربية' للغة العربية ").lower()

if lang_prompt == "english":  # English
    # ask user to enter a country name
    answer = screen.textinput(title="Country Name", prompt="Enter a country name\nWrite 'Exit' to quit").title()
    # importing countries data
    data = pd.read_csv('c_en.csv')
    country_list = data["country"].to_list()  # making a list of country names

    inserted_countries = []  # track the entered countries by user

    while answer != "Exit":
        if answer in country_list:  # checking if the user entered a country in the dataset
            # if the user answer correct extract that country info
            country_info = data[data.country == answer]
            # write country name on its location on map
            text.write_name(name=answer, x_position=country_info.x, y_position=country_info.y)
            inserted_countries.append(answer)  # add the answer to the inserted_countries list

        if len(inserted_countries) >= 22:  # when user enters all countries >> exit
            break
        # prompt the user again
        answer = screen.textinput(title=f"{len(inserted_countries)}/22 country", prompt="Enter a country name").title()


else:  # Arabic  # Default mode
    answer = screen.textinput(title="اسم الدولة", prompt="اكتب اسم دولة\nاكتب 'خروج' لمغادرة البرنامج").title()

    data = pd.read_csv('c_ar.csv')
    country_list = data["country"].to_list()
    inserted_countries = []

    while answer != "خروج":
        if answer in country_list:
            country_info = data[data.country == answer]
            text.write_name(name=answer, x_position=country_info.x, y_position=country_info.y)
            inserted_countries.append(answer)

        if len(inserted_countries) >= 22:
            break

        answer = screen.textinput(title=f"{len(inserted_countries)}/22 دولة ", prompt="اكتب اسم دولة").title()


if len(inserted_countries) < 22:  # if user failed to enter all the 22 countries
    countries_missed = list(set(country_list) - set(inserted_countries))       # get the missed countries
    pd.DataFrame(countries_missed).to_csv("missed countries.csv")  # put them in a csv file







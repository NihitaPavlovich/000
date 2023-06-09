from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox

# extract key from the configuration file
config_file = "config.txt"
config = ConfigParser()
config.read_file(open(config_file))
api_key = config.get('weather', 'api')
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

# explicit function to get weather details
def getweather(city):
    result = requests.get(url.format(city, api_key))

    if result:
        json = result.json()
        city = json['name']
        country = json['sys']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        weather1 = json['weather'][0]['main']
        final = [city, country, temp_kelvin, temp_celsius, weather1]
        return final
    else:
        print("NO Content Found")

# explicit function to search city
def search():
    city = city_text.get()
    weather = getweather(city)
    if weather:
        location_lbl['text'] = '{} ,{}'.format(weather[0], weather[1])
        temperature_label['text'] = str(weather[3]) + " градусов Цельсия"
        weather_l['text'] = weather[4]
    else:
        messagebox.showerror('Ошибка', "Невозможно найти информацию о погоде для {}".format(city))

# create object
app = Tk()
# add title
app.title("Weather App")
# adjust window size
app.geometry("600x300")

# add labels, buttons and text
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()
Search_btn = Button(app, text="Поиск погоды",
                    width=12, command=search)
Search_btn.pack()
location_lbl = Label(app, text="Местоположение", font=('bold', 20))
location_lbl.pack()
temperature_label = Label(app, text="")
temperature_label.pack()
weather_l = Label(app, text="")
weather_l.pack()
app.mainloop()

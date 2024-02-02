import requests
from tkinter import *

api_key = 'apikey'    # to operate this codes, you should enter a valid api key

#icons dict
weather_icons = {
    'clouds': 'Icons/icons8-clouds-40.png',
    'snow': 'Icons/icons8-snow-40.png',
    'clear': 'Icons/icons8-sun-40.png',
    'tornado': 'Icons/icons8-tornado-40.png',
    'thunderstorm': 'Icons/icons8-thunderstorm-40.png',
    'sleet': 'Icons/icons8-sleet-40.png',
    'partly Cloudy': 'Icons/icons8-partly-cloudy-day-40.png',
    'haze': 'Icons/icons8-haze-40.png',
    'hail': 'Icons/icons8-hail-40.png',
    'dusty': 'Icons/icons8-dust-40.png',
    'drizzle': 'Icons/icons8-drizzle-40.png',
    'air Quality': 'Icons/icons8-air-quality-40.png',
    'world': 'Icons/icons8-world-40.png',
    'clear sky': 'Icons/icons8-sun-40.png',
    'scattered clouds': 'Icons/icons8-partly-cloudy-day-40.png',
    'light rain': 'Icons/icons8-drizzle-40.png',
    'few clouds': 'Icons/icons8-partly-cloudy-day-40.png',
    'overcast clouds': 'Icons/icons8-clouds-40.png',
    'broken clouds': 'Icons/icons8-partly-cloudy-day-40.png',
    'light intensity drizzle rain': 'Icons/icons8-drizzle-40.png',
    'squalls': 'Icons/icons8-thunderstorm-40.png',
    'volcanic ash': 'Icons/icons8-dust-40.png',
    'dust': 'Icons/icons8-dust-40.png',
    'sand': 'Icons/icons8-dust-40.png',
    'fog': 'Icons/icons8-haze-40.png',
    'sand/dust whirls': 'Icons/icons8-air-quality-40.png',
    'smoke': 'Icons/icons8-haze-40.png',
    'mist': 'Icons/icons8-haze-40.png',
    'heavy shower snow': 'Icons/icons8-snow-40.png',
    'shower snow': 'Icons/icons8-snow-40.png',
    'light shower snow': 'Icons/icons8-snow-40.png',
    'rain and snow': 'Icons/icons8-sleet-40.png',
    'light rain and snow': 'Icons/icons8-sleet-40.png',
    'shower sleet': 'Icons/icons8-sleet-40.png',
    'light shower sleet': 'Icons/icons8-sleet-40.png',
    'heavy snow': 'Icons/icons8-snow-40.png',
    'light snow': 'Icons/icons8-snow-40.png',
    'ragged shower rain': 'Icons/icons8-drizzle-40.png',
    'heavy intensity shower rain': 'Icons/icons8-drizzle-40.png',
    'shower rain': 'Icons/icons8-drizzle-40.png',
    'light intensity shower rain': 'Icons/icons8-drizzle-40.png',
    'freezing rain': 'Icons/icons8-drizzle-40.png',
    'extreme rain': 'Icons/icons8-drizzle-40.png',
    'very heavy rain': 'Icons/icons8-drizzle-40.png',
    'heavy intensity rain': 'Icons/icons8-drizzle-40.png',
    'moderate rain': 'Icons/icons8-drizzle-40.png',
    'shower drizzle': 'Icons/icons8-drizzle-40',
    'heavy shower rain and drizzle': 'Icons/icons8-drizzle',
    'shower rain and drizzle': 'Icons/icons8-drizzle-40',
    'heavy intensity drizzle rain': 'Icons/icons8-drizzle-40',
    'drizzle rain': 'Icons/icons8-drizzle-40',
    'heavy intensity drizzle': 'Icons/icons8-drizzle-40',
    'light intensity drizzle': 'Icons/icons8-drizzle-40',
    'thunderstorm with heavy drizzle': 'Icons/icons8-thunderstorm-40.png',
    'thunderstorm with drizzle': 'Icons/icons8-thunderstorm-40',
    'thunderstorm with light drizzle': 'Icons/icons8-thunderstorm-40',
    'ragged thunderstorm': 'Icons/icons8-thunderstorm-40',
    'heavy thunderstorm': 'Icons/icons8-thunderstorm-40',
    'light thunderstorm': 'Icons/icons8-thunderstorm-40',
    'thunderstorm with heavy rain': 'Icons/icons8-thunderstorm-40',
    'thunderstorm with rain': 'Icons/icons8-thunderstorm-40',
    'thunderstorm with light rain': 'Icons/icons8-thunderstorm-40'

}

icon = None

#main fuction
def howistheweather():
    global icon
    city_name = city_entry.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        tempC = float(temp - 273)
        formattedTempC = '{:.2f}'.format(tempC)
        desc = data['weather'][0]['description'].lower()

        icon_file = weather_icons.get(desc, 'icons8-world-40.png')

        result_label.config(text=f'Temperature: {formattedTempC} C')
        result_label_2.config(text=f'Description: {desc}')

        icon = PhotoImage(file=icon_file)
        canvas.create_image(23, 25, anchor='center', image=icon)
        canvas.update_idletasks()

    else:
        result_label_2.config(text='Error fetching weather data')
        result_label.config(text='Please Enter Valid City')


#UserInterface
window = Tk()
window.config(background="orange")
window.title('HowIsTheWeather')
window.config(padx=30, pady=30)

canvas = Canvas(height=40, width=40, background="#FFAC1C")
canvas.pack()

city_info_label = Label(text="Enter City You Want", font=("Verdena", 20, "italic", "bold"))
city_info_label.config(bg="#FFAC1C")
city_info_label.pack()

result_label = Label(text="")
result_label.config(bg="#15BEFD")
result_label.pack()

result_label_2 = Label(text="")
result_label_2.config(bg="#15BEFD")
result_label_2.pack()

city_entry = Entry(width=30)
city_entry.config(bg="#FFAC1C", fg="#15BEFD")
city_entry.pack()

show_button = Button(text="SHOW", command=howistheweather)
show_button.config(fg="#15BEFD", font=("Verdena", 16, "bold", "italic"))
show_button.pack()


window.mainloop()
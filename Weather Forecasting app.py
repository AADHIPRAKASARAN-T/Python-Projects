from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import requests
API_KEY="21aa09b27f0a7e76afc28ed4adc11971"
BASE_URL="https://api.openweathermap.org/data/2.5/weather"
class WeatherApp(App):
    def build(self):
        self.layout=BoxLayout(orientation='vertical',padding=20,spacing=10)
        self.city_input=TextInput(hint_text="Eneter City Name",size_hint_y=None,height=50)
        self.get_weather_btn=Button(text="Get Weather",size_hint_y=None,height=50)
        self.result_label=Label(text="",halign='center',valign='middle')
        self.get_weather_btn.bind(on_press=self.get_weather)
        self.layout.add_widget(self.city_input)
        self.layout.add_widget(self.get_weather_btn)
        self.layout.add_widget(self.result_label)
        return self.layout
    def get_weather(self,instance):
        city=self.city_input.text
        if not city:
            self.result_label.text="Please enter a city name"
            return
        try:
            url=f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
            response=requests.get(url)
            data=response.json()
            if data["cod"]==200:
                temp=data["main"]["temp"]
                weather=data["weather"][0]["description"].capitalize()
                self.result_label.text=f"Weather in {city}:\n{weather},{temp}°C"
            else:
                self.result_label.text=f"City not found:{city}"
        except Exception as e:
            self.result_label.text="Error fetching Weather"
if __name__=="__main__":
    WeatherApp().run()


import kivy
import schedule
import time
from datetime import datetime
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from threading import Thread
from gtts import gTTS
from playsound import playsound
import tempfile
import pygame

kivy.require('2.0.0')

LANG_CODES = {
    'English': 'en',
    'Hindi': 'hi',
    'Tamil': 'ta',
    'Marathi': 'mr',
    'Gujarati': 'gu',
    'Bengali': 'bn',
    'French': 'fr',
    'German': 'de',
    'Spanish': 'es',
    'Chinese': 'zh-cn',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Russian': 'ru',
    'Arabic': 'ar',
}

DEFAULT_MESSAGE = "It's time for you to take your Medicine"
reminder_times = []
user_names = []

def validate_time(time_str):
    try:
        datetime.strptime(time_str, "%I:%M %p")
        return True
    except ValueError:
        return False

def send_reminder(language, names):
    lang_code = LANG_CODES.get(language, 'en')

    for name in names:
        message = f"{name}, {DEFAULT_MESSAGE}"
        
        
        tts = gTTS(text=message, lang=lang_code)
        
        
        temp_path = os.path.join(tempfile.gettempdir(), "reminder.mp3")
        tts.save(temp_path)

    
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(temp_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
        except Exception as e:
            print(f"Error playing sound: {e}")

        
        popup = Popup(title="Medicine Reminder",
                      content=Label(text=message),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

def run_reminders(language, names):
    while True:
        schedule.run_pending()
        time.sleep(1)

def schedule_reminder(language, names):
    for reminder_time in reminder_times:
        schedule.every().day.at(reminder_time).do(send_reminder, language, names)
    run_reminders(language, names)

class MedicineReminderApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label = Label(text="Enter Reminder time (12-hr format):", size_hint=(1, 0.1))
        self.layout.add_widget(self.label)

        self.time_input = TextInput(hint_text="03:00 PM", size_hint=(1, 0.1))
        self.layout.add_widget(self.time_input)

        self.name_input = TextInput(hint_text="Enter names separated by commas", size_hint=(1, 0.1))
        self.layout.add_widget(self.name_input)

        self.language_search = TextInput(hint_text="Search Language", size_hint=(1, 0.1))
        self.language_search.bind(text=self.on_search_language)
        self.layout.add_widget(self.language_search)

        self.language_spinner = Spinner(text='Select Language', values=list(LANG_CODES.keys()), size_hint=(1, 0.1))
        self.layout.add_widget(self.language_spinner)

        self.set_button = Button(text="Add Reminder", size_hint=(1, 0.1))
        self.set_button.bind(on_press=self.on_add_reminder)
        self.layout.add_widget(self.set_button)

        self.start_button = Button(text="Start all Reminders", size_hint=(1, 0.1))
        self.start_button.bind(on_press=self.on_start_reminders)
        self.layout.add_widget(self.start_button)

        return self.layout

    def on_search_language(self, instance, text):
        filtered = [lang for lang in LANG_CODES if text.lower() in lang.lower()]
        self.language_spinner.values = filtered if filtered else ["No Match"]

    def on_add_reminder(self, instance):
        reminder_time = self.time_input.text.strip()
        if validate_time(reminder_time):
            reminder_times.append(reminder_time)
            self.label.text = f"Added: {reminder_time}"
            self.time_input.text = ""
        else:
            self.label.text = "Invalid time. Use format like 03:00 PM"

    def on_start_reminders(self, instance):
        selected_language = self.language_spinner.text.strip()
        if selected_language == "Select Language":
            self.label.text = "Please select a Language"
            return

        if not reminder_times:
            self.label.text = "No Reminders added"
            return

        names_raw = self.name_input.text.strip()
        if not names_raw:
            self.label.text = "Please enter at least one name"
            return

        names = [name.strip() for name in names_raw.split(',') if name.strip()]

        reminder_thread = Thread(target=schedule_reminder, args=(selected_language, names))
        reminder_thread.daemon = True
        reminder_thread.start()

        self.label.text = f"Reminders running in {selected_language} for {', '.join(names)}"

if __name__ == "__main__":
    MedicineReminderApp().run()

    
                         

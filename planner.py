from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from datetime import datetime


class PlannerApp(App):
    def build(self):
        # Главный макет
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Поле для ввода заметки
        self.note_input = TextInput(hint_text="Введите заметку", size_hint_y=None, height=100)
        self.layout.add_widget(self.note_input)

        # Кнопка "Добавить заметку"
        add_note_button = Button(text="Добавить заметку", size_hint_y=None, height=50)
        add_note_button.bind(on_press=self.add_note)
        self.layout.add_widget(add_note_button)

        # Список заметок
        self.notes_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.notes_layout.bind(minimum_height=self.notes_layout.setter('height'))

        # ScrollView для списка заметок
        scroll_view = ScrollView(size_hint=(1, None), size=(self.layout.width, 300))
        scroll_view.add_widget(self.notes_layout)
        self.layout.add_widget(scroll_view)

        # Поле для выбора времени напоминания
        self.reminder_input = TextInput(hint_text="Введите время напоминания (ГГГГ-ММ-ДД ЧЧ:ММ)", size_hint_y=None, height=50)
        self.layout.add_widget(self.reminder_input)

        # Кнопка "Установить напоминание"
        set_reminder_button = Button(text="Установить напоминание", size_hint_y=None, height=50)
        set_reminder_button.bind(on_press=self.set_reminder)
        self.layout.add_widget(set_reminder_button)

        return self.layout

    def add_note(self, instance):
        """Добавляет заметку в список."""
        note_text = self.note_input.text
        if note_text:
            note_label = Label(text=note_text, size_hint_y=None, height=40)
            delete_button = Button(text="Удалить", size_hint_y=None, height=40)
            delete_button.bind(on_press=lambda btn: self.delete_note(note_label, delete_button))

            note_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            note_box.add_widget(note_label)
            note_box.add_widget(delete_button)

            self.notes_layout.add_widget(note_box)
            self.note_input.text = ""  # Очищаем поле ввода

    def delete_note(self, note_label, delete_button):
        """Удаляет заметку из списка."""
        self.notes_layout.remove_widget(note_label.parent)

    def set_reminder(self, instance):
        """Устанавливает напоминание."""
        reminder_time_str = self.reminder_input.text
        try:
            reminder_time = datetime.strptime(reminder_time_str, "%Y-%m-%d %H:%M")
            now = datetime.now()
            if reminder_time > now:
                delay = (reminder_time - now).total_seconds()
                Clock.schedule_once(lambda dt: self.show_reminder(), delay)
                self.reminder_input.text = "Напоминание установлено!"
            else:
                self.reminder_input.text = "Укажите время в будущем!"
        except ValueError:
            self.reminder_input.text = "Неверный формат времени!"

    def show_reminder(self):
        """Показывает напоминание."""
        from kivy.uix.popup import Popup
        from kivy.uix.label import Label

        popup = Popup(title='Напоминание',
                      content=Label(text='Время для вашей заметки!'),
                      size_hint=(0.8, 0.4))
        popup.open()


if __name__ == '__main__':
    PlannerApp().run()

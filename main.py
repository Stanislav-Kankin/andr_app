from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        # Создаем главный макет (вертикальный BoxLayout)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Добавляем приветствие
        greeting = Label(text="Привет! Это мое первое приложение на Kivy!", font_size=24)
        layout.add_widget(greeting)

        # Создаем кнопки
        left_button = Button(text="Левая кнопка", on_press=self.on_left_button_press)
        right_button = Button(text="Правая кнопка", on_press=self.on_right_button_press)

        # Добавляем кнопки в макет
        layout.add_widget(left_button)
        layout.add_widget(right_button)

        # Создаем Label для вывода текста
        self.output_label = Label(text="", font_size=20)
        layout.add_widget(self.output_label)

        return layout

    # Обработчики нажатий на кнопки
    def on_left_button_press(self, instance):
        self.output_label.text = "Вы нажали левую кнопку!"

    def on_right_button_press(self, instance):
        self.output_label.text = "Вы нажали правую кнопку!"


if __name__ == '__main__':
    MyApp().run()

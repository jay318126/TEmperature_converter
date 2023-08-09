from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class TempConverterApp(App):
    def build(self):
        self.box_layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        self.celsius_input = TextInput(multiline=False, input_type='number')
        self.result_label = Label(text="", font_size='30sp')

        self.box_layout.add_widget(Label(text="Enter Temperature in Celsius:"))
        self.box_layout.add_widget(self.celsius_input)
        self.box_layout.add_widget(self.result_label)

        self.celsius_input.bind(text=self.on_celsius_input_change)

        return self.box_layout

    def on_celsius_input_change(self, instance, value):
        try:
            celsius = float(value)
            fahrenheit = celsius * 9/5 + 32
            self.result_label.text = f"{celsius:.2f} °C is equal to {fahrenheit:.2f} °F"
        except ValueError:
            self.result_label.text = "Invalid input"


if __name__ == '__main__':
    TempConverterApp().run()

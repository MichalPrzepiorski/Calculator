from cnum import complex_number
import kivy
from dataclasses import replace
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
import re

#Zapisywanie wyniku do zmiennej
#logarytmy
#Liczby zespolone
#Ułamki
#Potęgi
#Pierwiastki "\u221A"
#set_precision

Window.size = (500,700)

class MyGrid(Widget):

    def clear(self):

        self.ids.calc_input.text = str(0)

    def clear_one_char(self):
        
        print = self.ids.calc_input.text 

        if print == "0":
            self.ids.calc_input.text = '0'
        else:
            char=self.ids.calc_input.text[:-1]

            self.ids.calc_input.text = char

    def dot(self):

            print = self.ids.calc_input.text

            if print.count('.') < len(re.split('\+|/|\*|-', print)): 
                self.ids.calc_input.text = f'{print}.'
            else:
                self.ids.calc_input.text = f'{print}'

    def complex_exp(self):

        print = self.ids.calc_input.text
        x = complex_number(complex(print)).obliczanie()
        v = "%f exp(%f)" % x
        self.ids.calc_input.text = v

    def math_sign(self, sign):

        print = self.ids.calc_input.text 

        if print == "0":
            print=self.ids.calc_input.text = ''
            print=self.ids.calc_input.text = f'{sign}'
        else:
            self.ids.calc_input.text = f'{print}{sign}'

    def plus_minus(self):

        print = self.ids.calc_input.text

        if "-" in print:
            self.ids.calc_input.text = print.replace("-", "", 1)
        else:
            self.ids.calc_input.text = f'-{print}'

    def button_press(self, button):

        print = self.ids.calc_input.text

        if print == "0":
            print=self.ids.calc_input.text = ''
            print=self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{print}{button}'

    def equal(self):
        
        print = self.ids.calc_input.text

        if 'ANS' in print:
            try:
                print=print           
                self.ids.calc_input.text = str(eval(print))
            except Exception:
                self.ids.excep_input.text = f'Zle wyrazenie, popraw skladnie!'
        else:
            try:           
                self.ids.calc_input.text = str(eval(print))
            except Exception:
                self.ids.excep_input.text = f'Zle wyrazenie, popraw skladnie!'

    def ANS(self):

            ANS = self.ids.calc_input.text
            self.ids.calc_input.text = f'ANS'


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
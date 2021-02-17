from kivy.app import App
from kivy.uix.label import Label
import time

name = input("What is your name? ")

class sanjai(App):

	def build(self):
		return Label(
			text = "Hello " + name
		)

demo = sanjai()
demo.run()
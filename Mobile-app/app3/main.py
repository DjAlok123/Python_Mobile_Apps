from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button


class DemoApp(App):
	def build(self):
		layout = AnchorLayout()
		bttn1 = Button(
			text = "Anchor Layout Demo",
			size_hint = (.2,.2),
			background_color = (0, 25, 1),
			color = (0, 0, 0, 1)

		)
		layout.add_widget(bttn1)
		return layout

DemoApp().run()
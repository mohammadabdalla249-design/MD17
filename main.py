from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MD17App(App):
    def build(self):
        self.title = "MD17 Store"
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        root.add_widget(Label(text="MD/17 STORE\nKhartoum", font_size=24, bold=True, size_hint_y=0.2))
        grid = GridLayout(cols=2, spacing=10, size_hint_y=0.6)
        products = {"Sugar": "1200 SDG", "Oil": "2500 SDG", "Flour": "1800 SDG", "Rice": "2000 SDG"}
        for name, price in products.items():
            btn = Button(text=f"{name}\n{price}")
            def make_click(n, p):
                return lambda x: setattr(self.info, 'text', f"Selected {n} - {p}")
            btn.bind(on_press=make_click(name, price))
            grid.add_widget(btn)
        root.add_widget(grid)
        self.info = Label(text="Select product", size_hint_y=0.2)
        root.add_widget(self.info)
        return root
MD17App().run()

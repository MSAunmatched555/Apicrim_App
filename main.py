# main.py
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivymd.app import MDApp

# Ajuste a janela só para teste desktop (remova se for rodar só no Android)
#Window.size = (720, 1440)

KV = f'''
#:import dp kivy.metrics.dp

Screen:
    canvas.before:
        Color:
            rgba: app.bg_color
        Rectangle:
            pos: self.pos
            size: self.size

    FloatLayout:
        # Logo (centralizado um pouco acima do centro)
        Image:
            source: "resources/Logo_Apicrim.png"
            size_hint: None, None
            size: dp(320), dp(320)
            keep_ratio: True
            allow_stretch: True
            pos_hint: {{'center_x': 0.5, 'center_y': 0.62}}

        # Botão preenchido (ENTRAR)
        MDFillRoundFlatButton:
            text: "ENTRAR"
            size_hint: 0.8, 0.1
            size: dp(220), dp(52)
            pos_hint: {{'center_x': 0.5, 'center_y': 0.35}}
            md_bg_color: app.primary_color
            text_color: app.on_primary_color
            radius: [dp(30),]
            font_style: "Button"
            on_release: app.on_enter()

        # Botão contorno (CADASTRE-SE)
        MDRoundFlatButton:
            text: "CADASTRE-SE"
            size_hint: None, None
            size: dp(220), dp(52)
            pos_hint: {{'center_x': 0.5, 'center_y': 0.22}}
            text_color: app.primary_color
            line_color: app.primary_color
            radius: [dp(30),]
            font_style: "Button"
            on_release: app.on_register()
'''

class TestApp(MDApp):
    # Cores como ListProperty para usar no KV (valores 0..1)
    bg_color = ListProperty([0.98, 0.87, 0.20, 1])       # amarelo do fundo
    primary_color = ListProperty([0.62, 0.26, 0.11, 1])  # marrom dos botões
    on_primary_color = ListProperty([1, 0.95, 0.84, 1])  # cor do texto do botão

    def build(self):
        # configurações de tema (opcional)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"  # só placeholder
        return Builder.load_string(KV)

    # handlers de exemplo
    def on_enter(self):
        print("Entrar pressionado")

    def on_register(self):
        print("Cadastre-se pressionado")

if __name__ == "__main__":
    TestApp().run()

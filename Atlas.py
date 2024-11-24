import webbrowser  # Importamos webbrowser para abrir enlaces

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation  # Importar para animaciones
from kivy.uix.behaviors import ButtonBehavior  # Permite que una imagen actúe como botón

# Configuración de la ventana
Window.clearcolor = (1, 1, 1, 1)  # Fondo blanco


# Clase para convertir una imagen en un botón
class ImageButton(ButtonBehavior, Image):
    pass


class AtlasApp(App):
    def build(self):
        self.root = FloatLayout()

        # Crear un layout principal para el contenido de la app
        main_layout = BoxLayout(orientation="vertical", spacing=10)

        # Crear la barra superior (barra con logo)
        top_bar = BoxLayout(orientation="horizontal", size_hint=(1, 0.1))

        # Layout para colocar la imagen del menú en la esquina superior izquierda
        menu_layout = BoxLayout(size_hint=(None, 1), size=(50, 50))  # Ajustar para tamaño fijo

        # Imagen del menú que actúa como botón
        menu_button = ImageButton(
            source="Menu.png",  # Imagen del menú
            allow_stretch=True,  # Permite el ajuste de tamaño
            keep_ratio=True,  # Mantiene la relación de aspecto
            size_hint=(None, None),
            size=(50, 50),  # Tamaño ajustado de la imagen
            on_press=self.toggle_menu  # Asignar acción al presionar
        )

        # Añadimos el botón con la imagen al layout
        menu_layout.add_widget(menu_button)

        top_bar.add_widget(menu_layout)
        top_bar.add_widget(Label())

        main_layout.add_widget(top_bar)

        # Texto de bienvenida
        main_layout.add_widget(Label(
            text="Bienvenido, coach",
            font_size="24sp",
            bold=True,
            color=(0, 0, 0, 1),  # Color negro
            size_hint=(1, 0.1),
            halign="center"
        ))

        # Imagen del logo principal
        main_layout.add_widget(Image(
            source="logo.png",
            size_hint=(1, 0.4)
        ))

        # Texto descriptivo
        main_layout.add_widget(Label(
            text="¿Buscas proteína,\npre-entrenos, suplementos,\naminoácidos y demás para tu día a día?",
            font_size="18sp",
            halign="center",
            valign="middle",
            color=(0, 0, 0, 1),  # Color negro
            size_hint=(1, 0.3),
        ))

        # Layout horizontal para los enlaces
        link_layout = BoxLayout(
            orientation="horizontal",
            size_hint=(None, None),  # Tamaño fijo
            height=40,
            width=300,  # Ajusta el ancho según necesites
            spacing=10,
            pos_hint={"center_x": 0.5, "y": 0.3}  # Centra horizontalmente y ajusta la posición vertical
        )

        # Estilo para los enlaces
        link_style = {
            'font_size': '16sp',
            'color': (0, 0, 1, 1),  # Azul para simular un enlace
        }

        # Enlace MDNLab
        btn1 = Label(
            text="MDNLab",
            font_size="16sp",
            color=(0, 0, 1, 1),  # Azul para simular un enlace
            halign="center",
            valign="middle",
            size_hint=(None, None),
            size=(120, 40),
            on_touch_down=self.on_link_click_mdnlab
        )

        # Enlace OptimumNutrition
        btn2 = Label(
            text="OptimumNutrition",
            font_size="16sp",
            color=(0, 0, 1, 1),  # Azul para simular un enlace
            halign="center",
            valign="middle",
            size_hint=(None, None),
            size=(180, 40),
            on_touch_down=self.on_link_click_optimum
        )

        # El símbolo "|" entre los enlaces
        separator = Label(
            text="|",
            font_size="16sp",
            halign="center",
            valign="middle",
            color=(0, 0, 0, 1),  # Negro para el separador
            size_hint=(None, None),
            size=(10, 40)
        )

        # Añadimos los enlaces y el separador al layout horizontal
        link_layout.add_widget(btn1)
        link_layout.add_widget(separator)
        link_layout.add_widget(btn2)

        # Añadimos el layout de enlaces al layout principal
        main_layout.add_widget(link_layout)

        # Menú lateral (Panel estático) con tamaño reducido
        self.menu = BoxLayout(orientation='vertical', size_hint=(None, 1), width=180, padding=(0, 50, 0, 420))  # Centrado con padding
        self.menu.add_widget(Button(text="Elemento 1", on_press=self.dummy_action, size_hint_y=None, height=40))  # Botones más pequeños
        self.menu.add_widget(Button(text="Elemento 2", on_press=self.dummy_action, size_hint_y=None, height=40))  # Botones más pequeños
        self.menu.add_widget(Button(text="Elemento 3", on_press=self.dummy_action, size_hint_y=None, height=40))  # Botones más pequeños

        # Fondo para el menú lateral (oscurecer la pantalla detrás del menú)
        self.menu_background = Widget(size_hint=(1, 1), pos_hint={'x': 0, 'top': 1})
        self.menu_background.color = (0, 0, 0, 0.5)  # Establecemos el color de fondo oscuro

        # Añadir todo a la interfaz principal
        self.root.add_widget(self.menu_background)
        self.root.add_widget(self.menu)
        self.root.add_widget(main_layout)

        # Inicialmente el menú está oculto (fuera de la pantalla)
        self.menu.x = -self.menu.width  # Mantener el menú fuera de la pantalla
        self.menu_background.opacity = 0  # Hacer que el fondo oscuro no sea visible

        return self.root

    def toggle_menu(self, instance):
        # Animación para mostrar u ocultar el menú lateral con suavidad
        if self.menu.x < 0:
            # Mostrar el menú (centrado en la izquierda)
            anim = Animation(x=0, duration=0.3)
            anim.start(self.menu)
            self.menu_background.opacity = 1  # Mostrar el fondo oscuro
        else:
            # Ocultar el menú (fuera de la pantalla)
            anim = Animation(x=-self.menu.width, duration=0.3)
            anim.start(self.menu)
            self.menu_background.opacity = 0  # Ocultar el fondo oscuro

    def open_link(self, url):
        # Usamos webbrowser para abrir un enlace en el navegador
        webbrowser.open(url)

    def on_link_click_mdnlab(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.open_link("https://mdnlabs.mx/?srsltid=AfmBOopmsd0ZBInbwLJqL6P-mrqgbr77jnCDu7M8ZMSzQc6xL7TWNp4O")

    def on_link_click_optimum(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.open_link("https://optimumnutrition.com")

    def dummy_action(self, instance):
        # Acción temporal para los botones del menú
        print(f"Acción de {instance.text}")


# Ejecutar la aplicación
if __name__ == "__main__":
    AtlasApp().run()

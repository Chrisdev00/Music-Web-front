import reflex as rx
import Music_Web.styles.styles as styles
from Music_Web.components.sidebar import sidebar
from Music_Web.components.main_section import main_container
from Music_Web.components.right_section import right_section



# class State(rx.State):
#     sidebar_visible: bool = False

#     def toogle_sidebar(self):
#         self.sidebar_visible = not self.sidebar_visible    


def index() -> rx.Component:
    return rx.grid(
        sidebar(),
        main_container(),        
        right_section(),
        class_name="container",
        style=styles.container_style,   
    )

    
    
base_style = {
    "margin": "0",
    "padding": "0",
    "box_sizing": "border-box",
    "font_family": "Roboto",    
    "background": "linear-gradient(#050505, #18181d)",    
    "height": "100vh" 
}

# Create app instance and add index page.
app = rx.App(
    style=base_style,
    stylesheets=[
        "estilos.css",
        "https://fonts.googleapis.com/css2?family=Roboto:wght@300;500&display=swap",
        "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
    ],
)
app.add_page(index)

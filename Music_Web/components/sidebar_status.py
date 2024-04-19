import reflex as rx

class State(rx.State):
    sidebar_visible: bool = False

    def toggle_sidebar(self):
        self.sidebar_visible = not self.sidebar_visible
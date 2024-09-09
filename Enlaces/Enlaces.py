"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from Enlaces.views.main.appreciation import appreciation
from Enlaces.views.main.projects import projects
from Enlaces.views.navbar import navbar
from Enlaces.views.main.home import home
from Enlaces.views.main.about import about
from Enlaces.views.footer import footer
from rxconfig import config

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        # rx.color_mode.button(position="bottom-right"),
        navbar(),
        home(),
        rx.divider(width="90%"),
        about(),
        rx.divider(width="90%"),
        projects(),
        rx.divider(width="90%"),
        appreciation(),
        footer(),
        width="100%",
        justify="center",
        align_items="center",
        bg=rx.color("sky",2),
    )
fonts=[
    "https://fonts.googleapis.com/css2?family=Ubuntu:wght@300;500;700&display=swap",
]
styles={
    "font-family":"Ubuntu",
}
app = rx.App(
    app_name="Café Con Palito",
    stylesheets=fonts,
    style=styles,
    theme=rx.theme(
        appearance="dark",
        accent_color="indigo",
        radius="medium"
    )
)
app.add_page(component=index,title="Café Con Palito | Main",description="Main Page")

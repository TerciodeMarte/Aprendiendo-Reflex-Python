import reflex as rx

from Enlaces.components.people.heading import heading
from Enlaces.components.people.media import media


def header(avatar:str,name:str,title:str,localitation:str,social:dict) -> rx.Component:
    return rx.hstack(
        rx.image(avatar,align="center",width="40%",height="auto",border_radius="1em",max_width="150px",alt=name),
        rx.vstack(
            heading(name, True),
            heading(title),
            rx.text(
                rx.icon("map-pin"),
                localitation,
                display="inherit"
            ),
            media(social),
            spacing="2",
        ),
        spacing="4",
        margin_top="6em",
        width="80%",
        justify="center",
        align_items="center",
    )
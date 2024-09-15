import reflex as rx
from Enlaces.components.people.heading import heading


def about_people(description: str) -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
            heading("Sobre mí"),
            rx.text(description,align="center",width="60%"),
            padding="1em",
            justify="center",
            align_items="center",
        )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
            heading("Sobre mí"),
            rx.text(description,align="center",width="80%"),
            align_items="center",
            justify="center",
        )
        ),
        justify="center",
        align_items="center",
        align="center",
        padding="1em",
        

    )
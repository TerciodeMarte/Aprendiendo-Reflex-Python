from datetime import datetime
import reflex as rx


def footer() -> rx.Component:
    
    return rx.vstack(
        rx.text("Made by Café Con Palito",align="center"),
        rx.text("With ❤️",align="center"),
        rx.image("../logo-negative-rb.png",
                width="8em",
                height="auto",
                align="center",
                alt="Café Con Palito Logo"
                ),
        bg=rx.color("accent", 3),
        width="100%",
        justify="center",
        align_items="center",
        padding="1em",
    )
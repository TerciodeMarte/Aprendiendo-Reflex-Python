import reflex as rx

from Enlaces.components.people.icon_button import icon_button

def media(social:dict) -> rx.Component:
    return rx.flex(
        icon_button(
            "mail",
            f"mailto:{social['email']}",
            social["email"],
            True
        ),
        rx.hstack(
            icon_button(
                "file-text",
                social["cv"]
            ),
            icon_button(
                "github",
                social["github"]
            ),
            icon_button(
                "linkedin",
                social["linkedin"]
            ),
            spacing="2"
        ),
        spacing="2",
        flex_direction=["column", "column", "row"]
    )
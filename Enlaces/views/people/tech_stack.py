import reflex as rx
from Enlaces.views.people.header import heading

def tech_stack(technologies: list) -> rx.Component:
    return rx.vstack(
        heading("Tecnologías"),
        rx.flex(
            *[
                rx.badge(
                    rx.box(
                        class_name=technology["icon"],
                        font_size="24px"
                    ),
                    rx.text(technology["name"]),
                    size="2"
                )
                for technology in technologies
            ],
            wrap="wrap",
            spacing="2",
            justify="center",
        ),
        spacing="4",
        justify="center",
        align_items="center",
    )
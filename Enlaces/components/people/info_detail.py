import reflex as rx

from Enlaces.components.people.icon_badge import icon_badge
from Enlaces.components.people.icon_button import icon_button

from Enlaces.data import Info


def info_detail(info: Info) -> rx.Component:
    return rx.flex(
        rx.hstack(
            icon_badge(info.icon),
            rx.vstack(
                rx.text(info.title,color_scheme="blue",font_weight="700"),
                rx.text(info.subtitle),
                rx.text(
                    info.description,
                    size="2",
                    color_scheme="gray"
                ),
                rx.cond(
                    info.technologies,
                    rx.flex(
                        *[
                            rx.badge(
                                rx.box(class_name=technology.icon),
                                technology.name,
                                color_scheme="gray"
                            )
                            for technology in info.technologies
                        ],
                        wrap="wrap",
                        spacing="2"
                    )
                ),
                rx.hstack(
                    rx.cond(
                        info.url != "",
                        icon_button(
                            "link",
                            info.url
                        )
                    ),
                    rx.cond(
                        info.github != "",
                        icon_button(
                            "github",
                            info.github
                        )
                    )
                ),
                spacing="2",
                width="100%"
            ),
            spacing="4",
            width="100%"
        ),
        rx.cond(
            info.image != "",
            rx.image(
                src=info.image,
                height="200px",
                width="auto",
                border_radius="2em",
                object_fit="cover"
            )
        ),
        rx.vstack(
            rx.cond(
                info.date != "",
                rx.badge(info.date)
            ),
            rx.cond(
                info.certificate != "",
                icon_button(
                    "shield-check",
                    info.certificate,
                    solid=True
                )
            ),
            spacing="2",
            align="end"
        ),
        flex_direction=["column-reverse", "row"],
        spacing="4",
        width="100%"
    )
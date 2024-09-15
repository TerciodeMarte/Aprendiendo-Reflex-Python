import reflex as rx

from Enlaces.components.people.heading import heading
from Enlaces.components.people.info_detail import info_detail

from Enlaces.data import Info

def info(title: str, info: list[Info]) -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                heading(title),
                rx.vstack(
                    *[
                        info_detail(item)
                        for item in info
                    ],
                spacing="4",
                width="100%",
                align_items="center"
                ),
        spacing="4",
        width="100%",
        align_items="center"
        )
    ),
    rx.mobile_and_tablet(
        rx.vstack(
            heading(title),
            rx.vstack(
                *[
                    info_detail(item)
                    for item in info
                ],
            spacing="4",
            width="100%",
            align_items="center"
            ),
        spacing="4",
        width="80%",
        align_items="center",
        )
    ),
    justify="center",
    align_items="center",
    padding="1em",
    )

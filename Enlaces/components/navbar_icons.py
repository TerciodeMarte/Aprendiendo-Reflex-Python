import reflex as rx

def navbar_icons_item(
    text: str, icon: str, url: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4", weight="medium"),
        ),
        href=url,
        font_height="300"
    )

def navbar_icons_only(
    icon: str, url: str
) -> rx.Component:
    return rx.link(
            rx.icon(icon),
        href=url,
        font_height="300"
    )

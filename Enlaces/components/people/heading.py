import reflex as rx


def heading(text: str, h1=False) -> rx.Component:
    return rx.heading(
        text,
        as_="h1" if h1 else "h2",
        size="8" if h1 else "6",
        color_scheme="blue",
        align="center",
    )
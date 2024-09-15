import reflex as rx

from Enlaces.components.navbar_icons import navbar_icons_item, navbar_icons_only

def navbar(index:bool) -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="../logo-simple-negative-rb.png",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                        alt="Logo con forma de taza de café",
                    ),
                    rx.heading(
                        "Café Con Palito", size="7", weight="bold",font_height="700"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_icons_item("Home", "home", "#home" if index else "/"),
                    navbar_icons_item("Sobre Nosotros", "users", "#about") if index else "",

                    navbar_icons_item(
                        "Proyectos", "square-kanban", "#projects"
                    ) if index else "",
                    navbar_icons_item(
                        "Agradecimientos", "heart-handshake", "#apreciation"
                    ) if index else "",
                    spacing="6",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.image(
                    src="../logo-simple-negative-rb.png",
                    width="2em",
                    height="auto",
                    border_radius="25%",
                    alt="Logo con forma de taza de café",
                ),
                rx.hstack(
                    navbar_icons_only("home", "#home" if index else "/"),
                    navbar_icons_only("users", "#about") if index else "",

                    navbar_icons_only(
                        "square-kanban", "#projects"
                    )if index else "",
                    navbar_icons_only(
                        "heart-handshake", "#apreciation"
                    )if index else "",
                    spacing="6",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        position="fixed",
        top="0px",
        width="100%",
        z_index=10,
    )
import reflex as rx

from Enlaces.components.profesores import profesores

def appreciation() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.heading("¡¡¡ GRACIAS !!!",color_scheme="blue",margin_top="1em",font_height="700",align="center"),
                rx.container(
                    rx.text("""Este espacio es para agradecer a todos los profesores y compañeros que nos han acompañado en nuestro camino. 
                    Sin vuestro apoyo, no podríamos haber llegado tan lejos.""",align="center"),
                    rx.text("""Muchas gracias a todos los profesores por la infinita paciencia, ya sabemos que no es fácil lidiar con nosotros, 
                        pero gracias a vosotros hemos aprendido mucho y hemos crecido como personas y como profesionales.""",align="center"),
                    rx.text("""El siguiente listado es para darles visibilidad y agradecerles por todo lo que han hecho por nosotros.""",align="center",margin_top="2em"),
                ),
                profesores(),
                rx.container(
                rx.text("""Y a nuestros compañeros, gracias por las risas, por los momentos difíciles que compartimos y por estar ahí incluso en los días más complicados. 
                        Aguantarnos mutuamente no siempre fue fácil, pero juntos superamos cada obstáculo, y eso nos hizo más fuertes.
                        Aunque cada uno siga su camino, siempre recordaremos los buenos momentos que pasamos juntos.""",align="center"),
                rx.text("""Recordad que siempre podéis contar con nosotros para lo que necesitéis. ¡Gracias por todo!""",align="center",color_scheme="blue",font_height="700",margin_top="1em"),
                margin_top="0"),
                rx.image("appreciation.jpg", width="40%",
                                height="auto",border_radius="1em",alt="Foto grupal de la promoción 2022-2024"),
                justify="center",
                align="center",
                align_items="center",
                id="apreciation",
                scroll_margin_top="4.5em",
                # bg=rx.color("indigo",2),
                width="100%",
                padding_bottom="1em",
                ),
            ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.heading("¡¡¡ GRACIAS !!!",color_scheme="blue",margin_top="1em",font_height="700",align="center"),
                rx.container(
                    rx.text("""Este espacio es para agradecer a todos los profesores y compañeros que nos han acompañado en nuestro camino. 
                    Sin vuestro apoyo, no podríamos haber llegado tan lejos.""",align="center"),
                    rx.text("""Muchas gracias a todos los profesores por la infinita paciencia, ya sabemos que no es fácil lidiar con nosotros, 
                        pero gracias a vosotros hemos aprendido mucho y hemos crecido como personas y como profesionales.""",align="center"),
                    rx.text("""El siguiente listado es para darles visibilidad y agradecerles por todo lo que han hecho por nosotros.""",align="center",margin_top="2em"),
                ),
                profesores(),
                rx.container(
                rx.text("""Y a nuestros compañeros, gracias por las risas, por los momentos difíciles que compartimos y por estar ahí incluso en los días más complicados. 
                        Aguantarnos mutuamente no siempre fue fácil, pero juntos superamos cada obstáculo, y eso nos hizo más fuertes.
                        Aunque cada uno siga su camino, siempre recordaremos los buenos momentos que pasamos juntos.""",align="center"),
                rx.text("""Recordad que siempre podéis contar con nosotros para lo que necesitéis. ¡Gracias por todo!""",align="center",color_scheme="blue",font_height="700",margin_top="1em"),
                margin_top="0"),
                rx.image("appreciation.jpg", width="80%",
                                height="auto",border_radius="1em",alt="Foto grupal de la promoción 2022-2024"),
                justify="center",
                align="center",
                align_items="center",
                
                # bg=rx.color("indigo",2),
                width="100%",
                padding_bottom="1em",
                ),
        ),
        id="apreciation",
        scroll_margin_top="4.5em",
    )

        

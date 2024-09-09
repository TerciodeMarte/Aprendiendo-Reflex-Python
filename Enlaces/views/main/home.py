import reflex as rx

def home() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
            rx.image("maquina.webp", max_width="20%",height="auto", margin="1em", border_radius="1em",alt="Máquina de café"),
            rx.vstack(
                rx.heading("¡Bienvenido a Café con Palito!",align="center",color_scheme="blue",font_height="700"),
                rx.container(
                    rx.text("Somos un equipo de trabajo que busca el desarrollo académico y profesional de sus integrantes.",align="center"),
                    rx.text("Nuestro objetivo es crear un ambiente de aprendizaje y colaboración para todas las personas que desean aprender y crecer en el mundo de la programación.",align="center",padding="1em"),
                    rx.text(
                        "Surgimos como equipo cuando empezamos a estudiar el CFGS Desarrollo de Aplicaciones Multiplataforma (DAM) durante el curso 2021-2022 en el ",
                        rx.link("IES Augusto González de Linares", href="https://www.iesaglinares.com/"),align="center",padding="1em"),
                    rx.text("""En nuestro tiempo libre nos juntábamos para tomar un café y hablar sobre las clases, nuestra broma era que el día que la máquina de café diera palitos, 
                            sería un día especial. Ya que esta nunca daba palitos.""",align="center",padding="1em"),
                    rx.text("En cuanto tuvimos la oportunidad de crear un proyecto en común, decidimos que nuestro nombre de equipo sería Café con Palito, para invocar a la fortuna.",align="center",padding="1em"),
                    max_width="75%",
                    font_height="300"
                    
                ),
                max_width="75%",
                align_items="center",
            ),
            justify="center",
            align_items="center",
            max_width="100%",
            margin_top="4.5em",
            margin_bottom="0",
            # bg=rx.color("sky",2),
            ),
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.heading("¡Bienvenido a Café con Palito!",align="center",height="auto",color_scheme="blue",font_height="700",alt="Máquina de café"),
                rx.container(
                rx.text("Somos un equipo de trabajo que busca el desarrollo académico y profesional de sus integrantes.",align="center"),
                rx.text("Nuestro objetivo es crear un ambiente de aprendizaje y colaboración para todas las personas que desean aprender y crecer en el mundo de la programación.",align="center",padding="1em"),
                rx.text(
                    "Surgimos como equipo cuando empezamos a estudiar el CFGS Desarrollo de Aplicaciones Multiplataforma (DAM) durante el curso 2021-2022 en el ",
                    rx.link("IES Augusto González de Linares", href="https://www.iesaglinares.com/"),align="center",padding="1em"),
                rx.text("""En nuestro tiempo libre nos juntábamos para tomar un café y hablar sobre las clases, nuestra broma era que el día que la máquina de café diera palitos, 
                        sería un día especial. Ya que esta nunca daba palitos.""",align="center",padding="1em"),
                rx.text("En cuanto tuvimos la oportunidad de crear un proyecto en común, decidimos que nuestro nombre de equipo sería Café con Palito, para invocar a la fortuna.",align="center",padding="1em"),
                width="80%",
                ),
                rx.image("maquina.webp", max_width="40%", margin="1em", border_radius="1em",align="center"),
                justify="center",
                align_items="center",
                align="center",
                width="100%",
                margin_top="5em",
                margin_bottom="0",
                # bg=rx.color("sky",2),
            ),
            
        id="home",
        scroll_margin_top="5em",
        )
    )
        
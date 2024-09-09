import reflex as rx

def profesores()->rx.Component:
    return rx.container(
        # DAM 1º Curso
        rx.text("Bases de Datos",color_scheme="blue",align="center"),
        rx.text("José Francisco Márquez Díaz",align="center"),
        rx.text("Programación",color_scheme="blue",align="center"),
        rx.text("Miguel Llano Ríos",align="center"),
        rx.text("Lenguaje de Marcas y Sistemas de Gestión",color_scheme="blue",align="center"),
        rx.text("Isabel de la Peña Muñoz",align="center"),
        rx.text("Jorge Jiménez Pérez-Higueras",align="center"),
        rx.hstack(
            rx.text("Paula Calva Villegas",align="center"),
            rx.link(rx.icon("linkedin"),href="https://www.linkedin.com/in/paula-calva-villegas-80519999/",is_external=True),
            align_items="center",
            justify="center"
        ),
        rx.text("Sistemas Informáticos",color_scheme="blue",align="center"),
        rx.text("Víctor Villegas Borge",align="center"),
        rx.hstack(
            rx.text("Roberto Macho González"),
            rx.link(rx.icon("linkedin"),href="https://www.linkedin.com/in/roberto-macho-gonz%C3%A1lez-01617660/",is_external=True),
            align_items="center",
            justify="center"
        ),
        rx.text("Entornos de Desarrollo",color_scheme="blue",align="center"),
        rx.text("Yolanda Moreno Aguero",align="center"),
        rx.hstack(
            rx.text("María Jesús Lobato Cucurull"),
            rx.link(rx.icon("linkedin"),href="https://www.linkedin.com/in/mjlobato/",is_external=True),
            align_items="center",
            justify="center"
        ),
        # DAM 2º Curso
        rx.text("Acceso a Datos",color_scheme="blue",align="center"),
        rx.text("Inmaculada Deseada Cerdeiriña Del Tio",align="center"),
        rx.text("Desarrollo de Interfaces",color_scheme="blue",align="center"),
        rx.hstack(
            rx.text("Carlos Solano Hidalgo"),
            rx.link(rx.icon("linkedin"),href="https://www.linkedin.com/in/carlos-solano-hidalgo-ba002857/",is_external=True),
            align_items="center",
            justify="center"
        ),
        rx.text("Programación de Servicios y Procesos",color_scheme="blue",align="center"),
        rx.hstack(
            rx.text("Joaquín Franco Ros"),
            rx.link(rx.icon("linkedin"),href="https://www.linkedin.com/in/joaqu%C3%ADn-franco-0144a4192/",is_external=True),
            align_items="center",
            justify="center"
        ),
        rx.text("Sistemas de Gestión Empresarial",color_scheme="blue",align="center"),
        rx.hstack(
            rx.text("Claudia Torre Celeizábal"),
            rx.link(rx.icon("linkedin"),href="https://www.linkedin.com/in/claudia-torre-celeiz%C3%A1bal/",is_external=True),
            align_items="center",
            justify="center"
        ),
        rx.text("Programación Multimedia y Dispositivos Móviles",color_scheme="blue",align="center"),
        rx.hstack(
            rx.text("Jonatan Pérez López"),
            rx.link(rx.icon("linkedin"),href="https://www.linkedin.com/in/jonatan-p-973499158/",is_external=True),
            align_items="center",
            justify="center"
        ),
        align_items="center",
        margin_top="0em",
        margin_bottom="0em",
        padding="0em"
    )
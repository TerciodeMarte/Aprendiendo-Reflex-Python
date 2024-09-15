"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from Enlaces.views.main.appreciation import appreciation
from Enlaces.views.main.projects import projects
from Enlaces.views.navbar import navbar
from Enlaces.views.main.home import home
from Enlaces.views.main.about import about
from Enlaces.views.footer import footer

from Enlaces.views.people.about_people import about_people
from Enlaces.views.people.header import header
from Enlaces.views.people.tech_stack import tech_stack
from Enlaces.views.people.info import info
from Enlaces.data import Info
from rxconfig import config

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        # rx.color_mode.button(position="bottom-right"),
        navbar(index=True),
        home(),
        rx.divider(width="90%"),
        about(),
        rx.divider(width="90%"),
        projects(),
        rx.divider(width="90%"),
        appreciation(),
        footer(),
        width="100%",
        justify="center",
        align_items="center",
        bg=rx.color("sky",2),
    )

def albano() -> rx.Component:
    # Curriculum de Albano
    return rx.vstack(
        navbar(index=False),
        header(avatar="../img/albano.webp",name="Albano Díez de Paulino",title="Backend Developer",localitation="Santander, Cantabria",
        social={
        "email": "albanodiezp@gmail.com",
        "cv": "/data/CV_Albano24_sep.pdf",
        "github": "https://github.com/TerciodeMarte",
        "linkedin": "https://www.linkedin.com/in/albano-diez/"
        }),
        about_people("Soy una persona resolutiva y organizada, siempre en busca de nuevos conocimientos que me permitan crecer y mejorar. Mi curiosidad y afán por aprender son los motores que impulsan mi desarrollo personal y profesional."),
        rx.divider(width="70%"),
        tech_stack([
            {"name":"Python","icon":"devicon-python-plain"},
            {"name":"FastAPI","icon":"devicon-fastapi-plain"},
            {"name":"Docker","icon":"devicon-docker-plain"},
            {"name":"PostgreSQL","icon":"devicon-postgresql-plain"},
            {"name":"MongoDB","icon":"devicon-mongodb-plain"},
            {"name":"Git","icon":"devicon-git-plain"},
            {"name":"GitLab","icon":"devicon-gitlab-plain"},
            {"name":"Linux","icon":"devicon-linux-plain"},
            {"name":"Azure","icon":"devicon-azure-plain"},
            {"name":"CI/CD","icon":"devicon-githubactions-plain"},
            {"name":"Docker","icon":"devicon-docker-plain"},
        ]),
        info("Experiencia",
            [
            Info(
                icon="brain-circuit",
                title="LIS Data Solutions",
                subtitle="Backend Developer",
                description="Desarrollo de software con IA para multiples soluciones.",
                date="06/2024 - Actualidad",
                certificate="https://www.lisdatasolutions.com/es/"
            ),
            Info(
                icon="database",
                title="LIS Data Solutions",
                subtitle="Trainee Backend Developer",
                description="Desarrollo de multiples soluciones backend.",
                date="10/2023 - 06/2024",
                certificate="https://www.lisdatasolutions.com/es/"
            ),
            Info(
                icon="speaker",
                title="Autonomo",
                subtitle="Técnico de sonido",
                description="Sonorización de eventos y conciertos.",
                date="05/2021 - 06/2023",
            ),
            Info(
                icon="cable",
                title="Circet España",
                subtitle="Técnico de fibra óptica",
                description="Instalación y mantenimiento de redes de fibra óptica.",
                date="08/2021 - 10/2021",
                certificate="https://www.circet.es/"
            )

            ]
            ),
        info("Formación",
            [
            Info(
                icon = "graduation-cap",
                title = "CFGS Desarrollo de Aplicaciones Multiplataforma",
                subtitle ="IES Augusto González de Linares",
                description= "Aprendizaje sobre desarrollo de aplicaciones multiplataforma,priorizando el desarrollo backend.",
                date= "09/2022 - 06/2024",
                certificate= "https://www.iesaglinares.com/"
            ),
            Info(
                icon = "graduation-cap",
                title = "CFGS Mantenimiento Electrónico",
                subtitle ="CIFPN1",
                description= "Aprendizaje sobre mantenimiento de equipos electrónicos.",
                date= "09/2017 - 06/2020",
                certificate= "https://cifp.es/"
            )
            ]),
        rx.divider(width="70%"),
        info("Proyectos",
            [
            Info(
                icon = "book-text",
                title = "Repositorío sobre el CFGS DAM",
                subtitle ="Conjunto de apuntes y ejercicios sobre el CFGS DAM.",
                description = "Repositorio publico con apuntes y ejercicios para ayudar a los alumnos del CFGS DAM.",
                technologies = [
                    {
                        "icon": "devicon-java-plain", 
                        "name": "Java"
                    },
                    {
                        "icon": "devicon-mysql-original",
                        "name": "MySQL"
                    },
                    {
                        "icon": "devicon-mongodb-plain",
                        "name": "MongoDB"
                    },
                    {
                        "icon": "devicon-spring-original",
                        "name": "Spring"
                    }
                ],
                image = "../data/dam.png",
                github = "https://github.com/TerciodeMarte/DAM"
            ),
            Info(
                icon = "panels-top-left",
                title = "Pagina web Café con Palito",
                subtitle ="Web del grupo de trabajo Café con Palito.",
                description = "Una web para mostrar los proyectos y curriculums de los integrantes del grupo de trabajo Café con Palito.",
                technologies = [
                    {
                        "icon": "devicon-python-plain", 
                        "name": "Reflex"
                    }
                ],
                image = "../data/web_cafe.png",
                github = "https://github.com/TerciodeMarte/Aprendiendo-Reflex-Python"
            ),
            ]),
        footer(),
        width="100%",
        justify="center",
        align_items="center",
        bg=rx.color("sky",2),
        
    )

def ramiro() -> rx.Component:
    # Curriculum de Albano
    return rx.vstack(
        navbar(index=False),
        header(avatar="../img/ramiro.webp",name="Ramiro Gutiérrez Valverde",title="Backend Developer",localitation="Santander, Cantabria",
        social={
        "email": "ramirogvalverde@gmail.com",
        "cv": "/data/CV_Ramiro24_sep.pdf",
        "github": "https://github.com/ramirogvalverde",
        "linkedin": "https://www.linkedin.com/in/ramirogvalverde/"
        }),
        about_people("Soy una persona creativa, resolutiva y que sabe trabajar en equipo. Me caracterizan mi capacidad de aprendizaje, adaptación y flexibilidad."),
        rx.divider(width="70%"),
        tech_stack([
            {"name":"Java SE","icon":"devicon-java-plain"},
            {"name":"SQL","icon":"devicon-azuresqldatabase-plain"},
            {"name":"Spring","icon":"devicon-spring-original"},
            {"name":"MongoDB","icon":"devicon-mongodb-plain"},
            {"name":"HTML","icon":"devicon-html5-plain"},
            {"name":"CSS","icon":"devicon-css3-plain"},
            {"name":"JavaScript","icon":"devicon-javascript-plain"},
            {"name":"Node npm","icon":"devicon-npm-original-wordmark"},
            {"name":"VueJS","icon":"devicon-vuejs-plain"},
            {"name":"Git","icon":"devicon-git-plain"},
            {"name":"GitLab","icon":"devicon-gitlab-plain"},
            {"name":"Docker","icon":"devicon-docker-plain"},

        ]),
        info("Experiencia",
            [
            Info(
                icon="database",
                title="CIC Consulting Informático",
                subtitle="Desarrollador backend junior",
                description="Desarrollo de multiples soluciones backend.",
                date="2024 - Actualidad",
                certificate="https://www.cic.es/"
            ),
            Info(
                icon="school",
                title="IES Nueve Valles",
                subtitle="Profesor sustituto de Educación Plástica",
                description="Impartir clases de Educación Plástica en ESO.",
                date="2023",
                certificate="https://www.educantabria.es/web/ies-nueve-valles"
            ),
            Info(
                icon="school",
                title="CEIP Ramón Laza",
                subtitle="Profesor de pintura para actividad extraescolar",
                description="Impartir clases de pintura a niños de primaria.",
                date="2010 -2021",
                certificate="https://www.educantabria.es/web/ceip-ramon-laza"
            ),
            Info(
                icon="school",
                title="IES Valle del Saja",
                subtitle="Profesor de refuerzo",
                description="Impartir clases de refuerzo a alumnos de ESO.",
                date="2008 -2021",
                certificate="https://www.iesvalledelsaja.com/"
            ),
            Info(
                icon="apple",
                title="Pablo Furer Sánchez S.L.",
                subtitle="Dependiente en frutería",
                description="Atención al cliente y venta de productos.",
                date="2008 -2024",
            ),
            Info(
                icon="school",
                title="CEIP Atalaya - CEIP San Antonio - CEIP El Salvador",
                subtitle="Profesor sustituto de Educación Plástica",
                description="Impartir clases de Educación Plástica en ESO.",
                date="2007",
            ),
            Info(
                icon="school",
                title="Talleres Artísticos Torre de la Vega",
                subtitle="Profesor de talleres de dibujo y pintura",
                description="Impartir clases de dibujo y pintura a niños y adultos.",
                date="2004-2006",
            ),
            ]
            ),
        info("Formación",
            [
            Info(
                icon = "backpack",
                title = "Bootcamp Aplicaciones empresariales web con tecnología java",
                subtitle ="CIC Consulting Informático",
                description= "Aprendizaje sobre desarrollo de aplicaciones empresariales web con tecnología java.",
                date= "2024",
                certificate= "https://www.cic.es/"
            ),
            Info(
                icon = "graduation-cap",
                title = "CFGS Desarrollo de Aplicaciones Multiplataforma",
                subtitle ="IES Augusto González de Linares",
                description= "Aprendizaje sobre desarrollo de aplicaciones multiplataforma,priorizando el desarrollo backend.",
                date= "2022 - 2024",
                certificate= "https://www.iesaglinares.com/"
            ),
            Info(
                icon = "camera",
                title = "Curso de fotografía",
                subtitle ="Centro Municipal de Formación de Torrelavega",
                description= "Aprendizaje sobre fotografía.",
                date= "2004 - 2005",
            ),
            Info(
                icon = "landmark",
                title = "Curso de aptitud pedagógica. CAP",
                subtitle ="Universidad de Salamanca",
                description= "Aprendizaje sobre pedagogía.",
                date= "2003 - 2004",
                certificate= "https://www.usal.es/"
            ),
            Info(
                icon = "landmark",
                title = "Licenciado en Bellas Artes. Especialidad dibujo",
                subtitle ="Universidad de Salamanca",
                description= "Licenciatura en Bellas Artes con especialidad en dibujo.",
                date= "1998 - 2003",
                certificate= "https://www.usal.es/"
            ),

            ]),
        footer(),
        width="100%",
        justify="center",
        align_items="center",
        bg=rx.color("sky",2),
        
    )


fonts=[
    "https://fonts.googleapis.com/css2?family=Ubuntu:wght@300;500;700&display=swap",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"
]
styles={
    "font-family":"Ubuntu",
}
app = rx.App(
    app_name="Café Con Palito",
    stylesheets=fonts,
    style=styles,
    theme=rx.theme(
        appearance="dark",
        accent_color="indigo",
        radius="medium"
    )
)
app.add_page(component=index,title="Café Con Palito | Main",description="Main Page",image="../logo-negative-rb.png",
        meta=[
        {"name": "og:title", "content": "Café Con Palito | Main"},
        {"name": "og:description", "content": "Main Page"},
        {"name": "og:image", "content": "../logo-negative-rb.png"},
    ])
app.add_page(component=albano,route="/albano",title="Café Con Palito | Albano",description="Albano's Page",image="../img/albano.webp",
        meta=[
        {"name": "og:title", "content": "Café Con Palito | Albano"},
        {"name": "og:description", "content": "Albano's Page"},
        {"name": "og:image", "content": "../img/albano.webp"},
    ])
app.add_page(component=ramiro,route="/ramiro",title="Café Con Palito | Ramiro",description="Ramiro's Page",image="../img/ramiro.webp",
        meta=[
        {"name": "og:title", "content": "Café Con Palito | Ramiro"},
        {"name": "og:description", "content": "Ramiro's Page"},
        {"name": "og:image", "content": "../img/ramiro.webp"},
    ])

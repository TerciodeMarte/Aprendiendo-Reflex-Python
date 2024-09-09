import reflex as rx

from Enlaces.components.project import project, project_mobile


def projects() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                project(
                    "Agilizando Mentes II",
                    """El proyecto consiste en desarrollar aplicaciones para mejorar el cálculo mental en alumnos de 1º a 4º de la ESO, 
                    con niveles de dificultad ajustados por curso. Incluirá ejercicios como divisiones simples, cálculo de restos y 
                    el uso del algoritmo de Euclides para el máximo común divisor. Además, las aplicaciones deberán ser accesibles y fáciles de usar.""",
                    "projects/agilizando.png",
                    "https://github.com/CafeConPalito/AgilizandoMentes2",
                    ["Toma de Requisitos","Trabajo en equipo","Gestión de recursos y tiempo", "Diseño UX/UI","Base de Datos Relacionales"],
                    ["MySQL","Docker","Java Swing","JDBC","JUnit","Maven"]
                ),
                project(
                    "Proyecto VaX",
                    """El proyecto busca crear un clon de Steam, una plataforma digital para comprar, descargar y gestionar videojuegos. 
                    Incluye funciones clave como cuentas de usuario, tienda virtual y descarga automática de juegos. 
                    El enfoque será ofrecer una interfaz intuitiva, segura y escalable, compatible con múltiples dispositivos.""",
                    "projects/vax.png",
                    "https://github.com/CafeConPalito/ProyectoVax",
                    ["Aplicaciones Cliente-Servidor", "Despliegue en Cloud","Diseño de Videojuegos","GitFlow"],
                    ["PostgreSQL","Sockets","JavaFX","Hibernate","AWS","Google Cloud"]
                ),
                project(
                    "Chikara",
                    """Este proyecto busca inspirar y motivar a las personas mediante contenido positivo, ayudando a superar desafíos diarios y alcanzar metas. 
                    Permite crear motivaciones personales, compartirlas públicamente para inspirar a otros y recibir apoyo de la comunidad para lograrlas.""",
                    "projects/chikara.png",
                    "https://github.com/CafeConPalito/TFCProyectoChikara",
                    ["Arquitectura de Microservicios", "API Rest","Base de datos no-relacionales", "Desarrollo de Aplicaciones Moviles", "Diseño de Interfaces Responsivas","CI/CD","Documentación de Proyectos"],
                    ["MongoDB","FastAPI","GitLab CI/CD","MS Azure","Kotlin"]
                ),
            width="100%",
            justify="center",
            align="center",
            align_items="center",
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                project_mobile(
                    "Agilizando Mentes II",
                    """El proyecto consiste en desarrollar aplicaciones para mejorar el cálculo mental en alumnos de 1º a 4º de la ESO, 
                    con niveles de dificultad ajustados por curso. Incluirá ejercicios como divisiones simples, cálculo de restos y 
                    el uso del algoritmo de Euclides para el máximo común divisor. Además, las aplicaciones deberán ser accesibles y fáciles de usar.""",
                    "projects/agilizando.png",
                    "https://github.com/CafeConPalito/AgilizandoMentes2",
                    ["Toma de Requisitos","Trabajo en equipo","Gestión de recursos y tiempo", "Diseño UX/UI","Base de Datos Relacionales"],
                    ["MySQL","Docker","Java Swing","JDBC","JUnit","Maven"]
                ),
                project_mobile(
                    "Proyecto VaX",
                    """El proyecto busca crear un clon de Steam, una plataforma digital para comprar, descargar y gestionar videojuegos. 
                    Incluye funciones clave como cuentas de usuario, tienda virtual y descarga automática de juegos. 
                    El enfoque será ofrecer una interfaz intuitiva, segura y escalable, compatible con múltiples dispositivos.""",
                    "projects/vax.png",
                    "https://github.com/CafeConPalito/ProyectoVax",
                    ["Aplicaciones Cliente-Servidor", "Despliegue en Cloud","Diseño de Videojuegos","GitFlow"],
                    ["PostgreSQL","Sockets","JavaFX","Hibernate","AWS","Google Cloud"]
                ),
                project_mobile(
                    "Chikara",
                    """Este proyecto busca inspirar y motivar a las personas mediante contenido positivo, ayudando a superar desafíos diarios y alcanzar metas. 
                    Permite crear motivaciones personales, compartirlas públicamente para inspirar a otros y recibir apoyo de la comunidad para lograrlas.""",
                    "projects/chikara.png",
                    "https://github.com/CafeConPalito/TFCProyectoChikara",
                    ["Arquitectura de Microservicios", "API Rest","Base de datos no-relacionales", "Desarrollo de Aplicaciones Moviles", "Diseño de Interfaces Responsivas","CI/CD","Documentación de Proyectos"],
                    ["MongoDB","FastAPI","GitLab CI/CD","MS Azure","Kotlin"]
                ),
            width="100%",
            justify="center",
            align="center",
            align_items="center",
            )
        
        ),
        id="projects",
        scroll_margin_top="4.5em",
    )
import reflex as rx

from Enlaces.components.infoperson import info_person


def about() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
            info_person(
                name="Albano Díez", 
                img="/img/albano.webp",
                title="Backend Developer & Tech Lead",
                description="""Es el Proyect Manager y Tech Lead del equipo. Sus tareas son las de coordinar el trabajo y 
                asegurarse que los proyectos tengan una buena calidad, tanto en el código como en la arquitectura.
                Siempre está mirando nuevas tecnologías.
                """,
                social_media=[
                    {"icon":"github","url":"https://github.com/TerciodeMarte"},
                    {"icon":"linkedin","url":"https://www.linkedin.com/in/albano-diez/"},
                    {"icon":"instagram","url":"https://www.instagram.com/terciodemarte/"}
                ],
                extra="/#"
                ),
            info_person(
                name="Carmen Barrios",
                img="/img/carmen.webp",
                title="Backend Developer",
                description="""
                Gracias a su experiencia en el mundo legal, se encarga de realizar la documentación técnica y legal de los proyectos.
                Además, aporta su visión de negocio para que los proyectos sean viables y tengan un impacto positivo en la sociedad.
                """,
                social_media=[
                    {"icon":"github","url":"https://github.com/CarmenBarrios"}
                ],
                extra="/#"
            ),
            info_person(
                name="Daniel Espinosa",
                img="/img/daniel.webp",
                title="Backend Developer & Mobile Developer",
                description="""
                Es el encargado de la parte de Backend de los proyectos. Se encarga de desarrollar la lógica de negocio y la base de datos.
                También se encarga de tomar decisiones sobre la arquitectura, mientras Albano se lo permite.
                """,
                social_media=[
                    {"icon":"github","url":"https://github.com/Daniel-Espinosa"},
                    {"icon":"linkedin","url":"https://www.linkedin.com/in/daniel-espinosa-garc%C3%ADa/"}
                ],
                extra="/#"
            ),
            info_person(
                name="Ramiro Gutierrez",
                img="/img/ramiro.webp",
                title="Backend Developer & UI/UX Designer",
                description="""
                Es el encargado de la parte de Frontend de los proyectos. Se encarga de diseñar y desarrollar la interfaz de usuario.
                Además, aporta su experiencia en el mundo del diseño para dar brillo y esplendor a los proyectos.
                """,
                social_media=[
                    {"icon":"github","url":"https://github.com/ramirogvalverde"},
                    {"icon":"linkedin","url":"https://www.linkedin.com/in/ramirogvalverde/"}
                ],
                extra="/#"
            ),
            width="100%",
            align_items="center",
            justify="center",
            # bg=rx.color("indigo",2),
            ),
        ),
        rx.mobile_and_tablet(
            rx.box(
                info_person(
                    name="Albano Díez", 
                    img="/img/albano.webp",
                    title="Backend Developer & Tech Lead",
                    description="""Es el Proyect Manager y Tech Lead del equipo. Sus tareas son las de coordinar el trabajo y 
                    asegurarse que los proyectos tengan una buena calidad, tanto en el código como en la arquitectura.
                    Siempre está mirando nuevas tecnologías.
                    """,
                    social_media=[
                        {"icon":"github","url":"https://github.com/TerciodeMarte"},
                        {"icon":"linkedin","url":"https://www.linkedin.com/in/albano-diez/"},
                        {"icon":"instagram","url":"https://www.instagram.com/terciodemarte/"}
                    ],
                    extra="/#"
                    ),
                info_person(
                    name="Carmen Barrios",
                    img="/img/carmen.webp",
                    title="Backend Developer",
                    description="""
                    Gracias a su experiencia en el mundo legal, se encarga de realizar la documentación técnica y legal de los proyectos.
                    Además, aporta su visión de negocio para que los proyectos sean viables y tengan un impacto positivo en la sociedad.
                    """,
                    social_media=[
                        {"icon":"github","url":"https://github.com/CarmenBarrios"}
                    ],
                    extra="/#"
                ),
                info_person(
                    name="Daniel Espinosa",
                    img="/img/daniel.webp",
                    title="Backend Developer & Mobile Developer",
                    description="""
                    Es el encargado de la parte de Backend de los proyectos. Se encarga de desarrollar la lógica de negocio y la base de datos.
                    También se encarga de tomar decisiones sobre la arquitectura, mientras Albano se lo permite.
                    """,
                    social_media=[
                        {"icon":"github","url":"https://github.com/Daniel-Espinosa"},
                        {"icon":"linkedin","url":"https://www.linkedin.com/in/daniel-espinosa-garc%C3%ADa/"}
                    ],
                    extra="/#"
                ),
                info_person(
                    name="Ramiro Gutierrez",
                    img="/img/ramiro.webp",
                    title="Backend Developer & UI/UX Designer",
                    description="""
                    Es el encargado de la parte de Frontend de los proyectos. Se encarga de diseñar y desarrollar la interfaz de usuario.
                    Además, aporta su experiencia en el mundo del diseño para dar brillo y esplendor a los proyectos.
                    """,
                    social_media=[
                        {"icon":"github","url":"https://github.com/ramirogvalverde"},
                        {"icon":"linkedin","url":"https://www.linkedin.com/in/ramirogvalverde/"}
                    ],
                    extra="/#"
                ),
                width="100%",
                align_items="center",
                justify="center",
                # bg=rx.color("indigo",2),
            ),
        ),
        id="about",
        scroll_margin_top="4.5em",
    )
    
            
import reflex as rx

def project(name: str,description:str,img:str,github:str,lessons:list,tecs:list) -> rx.Component:
    return rx.hstack(
		rx.image(img,width="40%",height="auto",margin="1em",border_radius="1em",alt=name),
        rx.container(
			rx.hstack(
				rx.heading(name,color_scheme="blue"),
				rx.link(rx.icon("github"),href=github,is_external=True),
			),
			rx.text(description),
			rx.hstack(
				rx.container(
					rx.heading("Lecciones Aprendidas",color_scheme="blue",margin_top="1em"),
					rx.unordered_list(
					*[rx.list.item(lesson) for lesson in lessons],
					),
				),
				rx.container(
					rx.heading("Tecnologías Aprendidas",color_scheme="blue",margin_top="1em"),
					rx.unordered_list(
					*[rx.list.item(tec) for tec in tecs],
					),
				),
				
			),
            width="60%"
        ),
        width="70%",
        justify="center",
    )

def project_mobile(name: str,description:str,img:str,github:str,lessons:list,tecs:list) -> rx.Component:
    return rx.vstack(
		rx.image(img,width="90%",height="auto",margin="1em",border_radius="1em",alt=name),
		rx.hstack(
			rx.heading(name,color_scheme="blue"),
			rx.link(rx.icon("github"),href=github,is_external=True),
		),
		rx.text(description,align="center"),
		rx.container(
			rx.heading("Lecciones Aprendidas",color_scheme="blue",margin_top="1em",align="center"),
			rx.container(
			*[rx.text(lesson,align="center") for lesson in lessons],
            padding="1em",
            margin="0em",
			),
            padding="0em",
            margin="0em",
		),
		rx.container(
			rx.heading("Tecnologías Aprendidas",color_scheme="blue",margin_top="1em",align="center"),
			rx.container(
			*[rx.text(tec,align="center") for tec in tecs],
            padding="1em",
            margin="0em",
			),
            padding="0em",
            margin="0em",
		),
        justify="center",
        align_items="center",
		width="70%"
        ),
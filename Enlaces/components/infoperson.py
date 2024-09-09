import reflex as rx


def info_person(name: str,title:str, img: str, description: str,social_media:list,extra:str) -> rx.Component:
    social_media_hstack:list=[]
    for social in social_media:
        social_media_hstack.append(rx.link(rx.icon(social["icon"]),href=social["url"],is_external=True))
    return rx.vstack(
        rx.image(img,align="center",width="40%",height="auto",border_radius="1em",alt=name),
        rx.container(
            rx.heading(name,color_scheme="blue",align="center",padding_top="1em"),
            rx.text(title,align="center",color_scheme="blue"),
            rx.text(description,align="center",padding="1em"),
            rx.hstack(*social_media_hstack,justify="center"),
            width="80%",
        ),
        justify="center",
        align_items="center",
        padding="1em",
    )
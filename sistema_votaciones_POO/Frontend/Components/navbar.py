import reflex as rx


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text("Bienvenido Usuario", margin= "5px"),
        rx.button("Resultados"),
        height= "auto",
        width= "100%",
        background_color= "#42f5c2",
        padding= "8px"
    )
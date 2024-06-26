import reflex as rx

from sistema_votaciones_POO.Backend.usuario import QueryUser


def navbar() -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.text(f"Bienvenido {QueryUser.users[0].nombre}", margin= "5px"),
        rx.chakra.button(
            "Resultados",
            on_click= rx.redirect(
                "/resultados"
            )),
        rx.chakra.button(
            "Cerrar Sesion",
            on_click= QueryUser.cerrarSesion()
        ),
        height= "auto",
        width= "100%",
        background_color= "#42f5c2",
        padding= "8px"
    )
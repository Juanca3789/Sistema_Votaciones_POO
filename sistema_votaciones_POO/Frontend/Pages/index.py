import reflex as rx

from sistema_votaciones_POO.Frontend.Components.loginModal import loginModal
from sistema_votaciones_POO.Frontend.Components.regModal import regModal


def index() -> rx.Component:
    return rx.center(
            rx.box(
                rx.vstack(
                    loginModal(
                        rx.button(
                            "Iniciar Sesión"
                        )
                    ),
                    regModal(
                        rx.button(
                            "Registro"
                        )
                    ),
                    align_items= "center"
                ),
                border_radius= "12px",
                border_color= "black",
                border_width= "1px",
                background_color= "#FEFFB7",
                padding= "1em",
                margin= "1em",
                width= "200px",
                height= "110px"
            )
        )
import reflex as rx

from sistema_votaciones_POO.Backend.usuario import QueryUser
from sistema_votaciones_POO.Frontend.Components.loginModal import loginModal
from sistema_votaciones_POO.Frontend.Components.regModal import regModal


def login() -> rx.Component:
    return rx.alert_dialog.root(
                rx.alert_dialog.content(
                    rx.heading("Sesión iniciada correctamente", margin= "6px"),
                    rx.text("Dirigiendo a la pagina principal", margin= "6px"),
                    rx.alert_dialog.action(
                        rx.button(
                            "Aceptar",
                            on_click= rx.redirect(
                                "/votacion"
                            )
                        )
                    )
                ),
                open= QueryUser.aux1
            )

def register() -> rx.Component:
    return rx.alert_dialog.root(
                rx.alert_dialog.content(
                    rx.heading("Usuario registrado correctamente", margin= "6px"),
                    rx.text("Por favor, inicie sesión para continuar", margin= "6px"),
                    rx.alert_dialog.action(
                        rx.button(
                            "Aceptar",
                            on_click= QueryUser.onReg()
                        )
                    )
                ),
                open= QueryUser.aux2
            )

def index() -> rx.Component:
    return rx.center(
            rx.card(
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
                margin= "1em"
            ),
            login(),
            register()
        )
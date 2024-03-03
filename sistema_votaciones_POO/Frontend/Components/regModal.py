import reflex as rx

from sistema_votaciones_POO.Frontend.Components.loginModal import loginModal


def regModal(trigger: rx.Component) -> rx.Component:
    return rx.alert_dialog.root(
                rx.alert_dialog.trigger(
                    trigger
                ),
                rx.alert_dialog.content(
                    rx.hstack(
                        rx.alert_dialog.cancel(
                            rx.button(
                                rx.icon("x-circle")
                            )
                        ),
                        rx.alert_dialog.title("Registrate para votar", margin_top= "0.35em")
                    ),
                    rx.alert_dialog.description(
                        rx.text("Ya tienes una cuenta? ",
                                loginModal(rx.link("Inicia sesión aquí"))
                            )
                    ),
                    rx.vstack(
                        rx.input(placeholder= "Numero de cedula"),
                        rx.input(placeholder= "Nombre completo"),
                        rx.input(placeholder= "Contraseña"),
                        rx.alert_dialog.action(
                            rx.button("Registro")
                        )
                    )
                )
            )
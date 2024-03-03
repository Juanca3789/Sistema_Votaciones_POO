import reflex as rx


def loginModal(trigger: rx.Component) -> rx.Component:
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
                        rx.alert_dialog.title("Inicia sesión para votar", margin_top= "0.35em")
                    ),
                    rx.alert_dialog.description(
                        rx.text("Aún no tienes una cuenta? ",
                                rx.alert_dialog.root(
                                    rx.alert_dialog.trigger(
                                        rx.link("Registrate aquí")
                                    ),
                                    rx.alert_dialog.content(
                                        rx.hstack(
                                            rx.alert_dialog.cancel(
                                                rx.button(
                                                    rx.icon("x-circle")
                                                )
                                            ),
                                            rx.alert_dialog.title("Registrate para votar")
                                        ),
                                        rx.spacer(),
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
                        )
                    ),
                    rx.vstack(
                        rx.input(placeholder= "Numero de cedula"),
                        rx.input(placeholder="Contraseña"),
                        rx.alert_dialog.action(
                            rx.button("Ingresar")
                        )
                    )
                )
            )
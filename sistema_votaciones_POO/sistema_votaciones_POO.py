import reflex as rx


class State(rx.State):
    """The app state."""

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
                        rx.alert_dialog.title("Inicia sesión para votar")
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
                        rx.alert_dialog.title("Registrate para votar")
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

app = rx.App()
app.add_page(index)
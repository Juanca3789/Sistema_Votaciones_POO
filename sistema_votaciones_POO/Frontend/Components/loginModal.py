import reflex as rx

from sistema_votaciones_POO.Backend.usuario import QueryUser


def loginModal(trigger: rx.Component) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(trigger),
        rx.alert_dialog.content(
            rx.hstack(
                rx.alert_dialog.cancel(
                    rx.button(rx.icon("x-circle"))
                ),
                rx.alert_dialog.title("Inicia sesión para votar", margin_top="0.35em")
            ),
            rx.alert_dialog.description(
                rx.text("Aún no tienes una cuenta? ",
                        regModal(rx.link("Regístrate aquí"))
                )
            ),
            rx.vstack(
                rx.input(
                    placeholder="Número de cédula",
                    on_change=QueryUser.set_num_cedula,
                    type="number"
                ),
                rx.input(
                    placeholder="Contraseña",
                    on_change=QueryUser.set_clave,
                    type="password"
                ),
                rx.alert_dialog.action(
                    rx.button(
                        "Ingresar",
                        on_click=QueryUser.iniciarSesion,
                        type="reset"
                    )
                )
            )
        )
    )

def regModal(trigger: rx.Component) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(trigger),
        rx.alert_dialog.content(
            rx.hstack(
                rx.alert_dialog.cancel(
                    rx.button(rx.icon("x-circle"))
                ),
                rx.alert_dialog.title("Regístrate para votar", margin_top="0.35em")
            ),
            rx.vstack(
                rx.input(
                    placeholder="Número de cédula",
                    on_change=QueryUser.set_num_cedula,
                    type="number"
                ),
                rx.input(
                    placeholder="Nombre completo",
                    on_change=QueryUser.set_nombre,
                    type="text"
                ),
                rx.input(
                    placeholder="Contraseña",
                    on_change=QueryUser.set_clave,
                    type="password"
                ),
                rx.alert_dialog.action(
                    rx.button(
                        "Registro",
                        on_click=QueryUser.nuevoUsuario,
                        type="reset"
                    )
                )
            )
        )
    )
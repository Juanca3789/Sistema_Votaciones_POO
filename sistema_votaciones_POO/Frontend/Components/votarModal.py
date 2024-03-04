import reflex as rx


def votarModal(trigger: rx.Component) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            trigger
        ),
        rx.alert_dialog.content(
            rx.text.strong("Seleccione el medio por el que se enteró del candidato:"),
            rx.radio(["Televisión", "Radio", "Internet"], default_value= "Televisión"),
            rx.hstack(
                rx.alert_dialog.cancel(
                    rx.button("Regresar")
                ),
                rx.alert_dialog.action(
                    rx.button("Votar")
                ),
                margin_top= "8px"
            )
        )
    )

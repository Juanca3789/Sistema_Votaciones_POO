import reflex as rx

from sistema_votaciones_POO.Backend.votaciones import candidatos, votaciones


def votarModal(trigger: rx.Component, cand: candidatos) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            trigger
        ),
        rx.alert_dialog.content(
            rx.text.strong("Seleccione el medio por el que se enteró del candidato:"),
            rx.select(
                ["Television", "Radio", "Internet"],
                default_value= "Television",
                on_change= votaciones.set_medio_comunicacion
            ),
            rx.hstack(
                rx.alert_dialog.cancel(
                    rx.button("Regresar")
                ),
                rx.alert_dialog.action(
                    rx.button(
                        "Votar",
                        on_click= votaciones.votar
                    )
                ),
                margin_top= "8px"
            )

        ),
        on_open_change= votaciones.setCandidato(cand.id)
    )

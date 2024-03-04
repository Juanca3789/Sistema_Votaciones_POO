import reflex as rx


def detailsModal(trigger: rx.Component) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            trigger
        ),
        rx.alert_dialog.content(
            rx.flex(
                rx.hstack(
                    rx.image(src= "/images.png"),
                    rx.vstack(
                        rx.heading("Candidato #1"),
                        rx.text(rx.text.strong("Genero: "), "Masculino"),
                        rx.text(rx.text.strong("Edad: "), "52"),
                        rx.text(rx.text.strong("Partido politico: "), "Comunista"),
                        rx.text(rx.text.strong("Costo de campaña: "), "2'000.000"),
                        rx.text(rx.text.strong("Cantidad de votos: "), "0"),
                        rx.text(rx.text.strong("Porcentaje de votos: "), "0%"),
                        rx.alert_dialog.cancel(
                            rx.button("Regresar")
                        )
                    )
                ),
                spacing="2"
            )
        ),
    )
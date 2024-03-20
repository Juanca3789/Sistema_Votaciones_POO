import reflex as rx

from sistema_votaciones_POO.Backend.votaciones import candidatos


def detailsModal(trigger: rx.Component, cand: candidatos) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            trigger
        ),
        rx.alert_dialog.content(
            rx.flex(
                rx.hstack(
                    rx.image(src= {cand.imagen}),
                    rx.vstack(
                        rx.heading(cand.nombre),
                        rx.text(rx.text.strong("Genero: "), f"{cand.genero}"),
                        rx.text(rx.text.strong("Edad: "), f"{cand.edad}"),
                        rx.text(rx.text.strong("Partido politico: "), f"{cand.partido}"),
                        rx.text(rx.text.strong("Costo de campaña: "), f"{cand.costo_campaña}"),
                        rx.text(rx.text.strong("Cantidad de votos: "), f"{cand.cant_votos}"),
                        rx.text(rx.text.strong("Porcentaje de votos: "), f"{cand.pvotos}"),
                        rx.alert_dialog.cancel(
                            rx.button("Regresar")
                        )
                    )
                ),
                spacing="2"
            )
        ),
    )
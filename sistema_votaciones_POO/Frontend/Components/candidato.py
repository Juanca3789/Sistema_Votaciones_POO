import reflex as rx

from sistema_votaciones_POO.Frontend.Components.detailsModal import \
    detailsModal
from sistema_votaciones_POO.Frontend.Components.votarModal import votarModal


def candidato() -> rx.Component:
    return rx.card(
                    rx.flex(
                        rx.box(
                            rx.heading(
                                "Candidato #1",
                                align= "center"
                            ),
                            rx.image(
                                src="/images.png",
                                align= "center"
                            ),
                            rx.text(
                                "Partido Politico",
                                align= "center"
                            ),
                            rx.hstack(
                                detailsModal(
                                    rx.button(
                                        "Detalles"
                                    )
                                ),
                                votarModal(
                                    rx.button(
                                        "Votar"
                                    )
                                ),
                                float= "right"
                            )
                        ),
                        spacing="2",
                    ),
                    as_child=True,
                )
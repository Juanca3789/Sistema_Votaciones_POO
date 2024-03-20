import reflex as rx

from sistema_votaciones_POO.Backend.votaciones import candidatos
from sistema_votaciones_POO.Frontend.Components.detailsModal import \
    detailsModal
from sistema_votaciones_POO.Frontend.Components.votarModal import votarModal


def candidato(cand: candidatos) -> rx.Component:
    return rx.card(
                    rx.flex(
                        rx.box(
                            rx.heading(
                                f"{cand.nombre}",
                                align= "center"
                            ),
                            rx.image(
                                src=f"{cand.imagen}",
                                align= "center",
                                margin= "10px"
                            ),
                            rx.text(
                                f"Partido: {cand.partido}",
                                align= "center"
                            ),
                            rx.hstack(
                                detailsModal(
                                    rx.button(
                                        "Detalles"
                                    ),
                                    cand
                                ),
                                votarModal(
                                    rx.button(
                                        "Votar"
                                    ),
                                    cand
                                ),
                                float= "right",
                                margin_top= "4px"
                            )
                        ),
                        spacing="2",
                    ),
                    as_child=True,
                )
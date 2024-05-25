import reflex as rx

from sistema_votaciones_POO.Backend.votaciones import candidatos
from sistema_votaciones_POO.Frontend.Components.detailsModal import \
    detailsModal
from sistema_votaciones_POO.Frontend.Components.votarModal import votarModal


def candidato(cand: candidatos) -> rx.Component:
    return rx.chakra.card(
                    rx.chakra.flex(
                        rx.chakra.box(
                            rx.chakra.heading(
                                f"{cand.nombre}",
                                align= "center"
                            ),
                            rx.chakra.image(
                                src=f"{cand.imagen}",
                                align= "center",
                                margin= "10px"
                            ),
                            rx.chakra.text(
                                f"Partido: {cand.partido}",
                                align= "center"
                            ),
                            rx.chakra.hstack(
                                detailsModal(
                                    rx.chakra.button(
                                        "Detalles"
                                    ),
                                    cand
                                ),
                                votarModal(
                                    rx.chakra.button(
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
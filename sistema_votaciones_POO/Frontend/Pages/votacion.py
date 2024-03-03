import reflex as rx

from sistema_votaciones_POO.Frontend.Components.candidato import candidato
from sistema_votaciones_POO.Frontend.Components.navbar import navbar


def votacion() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.flex(
                candidato(),
                candidato(),
                candidato(),
                candidato(),
                spacing="2",
                align= "center",
                justify= "center",
                wrap= "wrap"
            ),
            margin_top= "8px"
        )
    )
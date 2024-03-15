import reflex as rx

from sistema_votaciones_POO.Backend.usuario import QueryUser
from sistema_votaciones_POO.Backend.votaciones import votaciones
from sistema_votaciones_POO.Frontend.Components.candidato import candidato
from sistema_votaciones_POO.Frontend.Components.navbar import navbar


def votacion() -> rx.Component:
    return rx.cond(
        QueryUser.aux1,
        rx.box(
            navbar(),
            rx.center(
                rx.flex(
                    candidato(votaciones.candidaturas[0]),
                    candidato(votaciones.candidaturas[1]),
                    candidato(votaciones.candidaturas[2]),
                    candidato(votaciones.candidaturas[3]),
                    spacing="2",
                    align= "center",
                    justify= "center",
                    wrap= "wrap"
                ),
                margin_top= "8px"
            )
        ),
        rx.script(
            "window.location.assign('http://localhost:3000/')"
        )
    )
        
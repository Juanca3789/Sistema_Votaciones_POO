import reflex as rx

from sistema_votaciones_POO.Backend.usuario import QueryUser
from sistema_votaciones_POO.Backend.votaciones import votaciones
from sistema_votaciones_POO.Frontend.Components.navbar import navbar
from sistema_votaciones_POO.Frontend.Components.tablaPosiciones import \
    tablaPosiciones


def resultados() -> rx.Component:
    return rx.cond(
        QueryUser.aux1,
        rx.box(
            navbar(),
            tablaPosiciones(votaciones.candidaturas),
            rx.button(
                "Vaciar Urna",
                on_click=votaciones.vaciarUrna,
                margin_top="10px"
            )
        ),
        rx.script("window.location.assign('http://localhost:3000/')")
    )

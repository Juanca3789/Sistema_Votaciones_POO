import reflex as rx

from sistema_votaciones_POO.Frontend.Components.navbar import navbar
from sistema_votaciones_POO.Frontend.Components.tablaPosiciones import \
    tablaPosiciones


def resultados() -> rx.Component:
    return rx.box(
        navbar(),
        tablaPosiciones()
    )
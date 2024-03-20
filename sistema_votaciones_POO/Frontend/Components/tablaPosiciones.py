from datetime import datetime

import reflex as rx

from sistema_votaciones_POO.Backend.votaciones import candidatos


def rowCandidato(icon: str, candidato: candidatos) -> rx.Component:
    return rx.table.row(
                rx.table.cell(
                    rx.icon(icon)
                ),
                rx.table.cell(
                    rx.text(f"{candidato.nombre}")
                ),
                rx.table.cell(
                    rx.text(f"{candidato.cant_votos} votos")
                ),
                rx.table.cell(
                    rx.text(f"{candidato.pvotos}%")
                )
            )

def tablaPosiciones(lcandidatos: list[candidatos]) -> rx.Component:
    return rx.flex(
        rx.heading("Resultados actuales"),
        rx.text(f"La siguiente tabla muestra los resultados hasta el dia {datetime.now().date()}"),
        rx.table.root(
            rx.table.body(
                rx.table.row(
                    rx.table.cell(
                        rx.text.strong("Pos.")
                    ),
                    rx.table.cell(
                        rx.text.strong("Nombre Candidato")
                    ),
                    rx.table.cell(
                        rx.text.strong("# Votos")
                    ),
                    rx.table.cell(
                        rx.text.strong("% Votos")
                    )
                ),
                rowCandidato("tally-1", lcandidatos[0]),
                rowCandidato("tally-2", lcandidatos[1]),
                rowCandidato("tally-3", lcandidatos[2]),
                rowCandidato("tally-4", lcandidatos[3])
            )
        ),
        direction= "column",
        margin_top= "6px",
        margin_x= "15px"
    )
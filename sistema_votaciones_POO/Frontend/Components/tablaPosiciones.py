from datetime import datetime

import reflex as rx


def rowCandidato(icon: str) -> rx.Component:
    return rx.table.row(
                rx.table.cell(
                    rx.icon(icon)
                ),
                rx.table.cell(
                    rx.text("Candidato #1")
                ),
                rx.table.cell(
                    rx.text(f"{0} votos")
                ),
                rx.table.cell(
                    rx.text(f"{0}%")
                )
            )

def tablaPosiciones() -> rx.Component:
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
                rowCandidato("tally-1"),
                rowCandidato("tally-2"),
                rowCandidato("tally-3"),
                rowCandidato("tally-4")
            )
        ),
        direction= "column",
        margin_top= "6px",
        margin_x= "15px"
    )
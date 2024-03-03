import reflex as rx


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
                                rx.button(
                                    "Detalles"
                                ),
                                rx.button(
                                    "Votar"
                                ),
                                float= "right"
                            )
                        ),
                        spacing="2",
                    ),
                    as_child=True,
                )
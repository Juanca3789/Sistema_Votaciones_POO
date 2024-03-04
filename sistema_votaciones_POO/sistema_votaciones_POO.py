import reflex as rx

from sistema_votaciones_POO.Frontend.Pages.index import index
from sistema_votaciones_POO.Frontend.Pages.resultados import resultados
from sistema_votaciones_POO.Frontend.Pages.votacion import votacion


class State(rx.State):
    """The app state."""

app = rx.App()
app.add_page(index)
app.add_page(votacion)
app.add_page(resultados)
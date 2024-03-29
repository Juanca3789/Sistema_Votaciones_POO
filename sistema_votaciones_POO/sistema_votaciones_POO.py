import reflex as rx

from sistema_votaciones_POO.Backend.votaciones import votaciones
from sistema_votaciones_POO.Frontend.Pages.index import index
from sistema_votaciones_POO.Frontend.Pages.resultados import resultados
from sistema_votaciones_POO.Frontend.Pages.votacion import votacion

app = rx.App()
app.add_page(index)
app.add_page(votacion, on_load= votaciones.setVotosCandidato())
app.add_page(resultados)
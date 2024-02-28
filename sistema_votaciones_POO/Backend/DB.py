import reflex as rx


class Candidato(rx.Model, table = True):
    nombre: str
    edad: int
    partido: str
    costo_campania: float
    votos_obtenidos: int

class User(rx.Model, table = True):
    nombre: str
    num_cedula: int
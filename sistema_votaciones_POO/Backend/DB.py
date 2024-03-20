import reflex as rx


class User(rx.Model, table = True):
    nombre: str
    num_cedula: int
    clave: str

class Votos(rx.Model, table= True):
    id_candidato: int
    medio_comunicacion: str
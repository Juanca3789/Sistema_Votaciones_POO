import reflex as rx


class User(rx.Model, table = True):
    nombre: str
    num_cedula: int
    clave: str
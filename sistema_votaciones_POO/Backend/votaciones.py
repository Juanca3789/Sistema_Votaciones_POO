import reflex as rx


class candidatos(rx.Base):
        id: str
        nombre: str
        imagen: str
        partido: str
        genero: str
        edad: int
        costo_campaña: int
        cant_votos: str

class votaciones(rx.State):
    candidaturas : list[candidatos] = [
        candidatos(id= 1, nombre= "Stalin", imagen= "/stalin.png", partido= "Comunista", genero= "Hombre", edad= 40, costo_campaña= 0, cant_votos= 0),
        candidatos(id= 2, nombre= "Hitler", imagen= "/fuhrer.png", partido= "Nazi", genero= "Hombre", edad= 45, costo_campaña= 0, cant_votos= 0),
        candidatos(id= 3, nombre= "Richard", imagen= "/images.png", partido= "GAY", genero= "Hombre", edad= 24, costo_campaña= 0, cant_votos= 0),
        candidatos(id= 4, nombre= "José", imagen= "/images.png", partido= "LGBTIQ+", genero= "No binario", edad= 20, costo_campaña= 0, cant_votos= 0)
        ]
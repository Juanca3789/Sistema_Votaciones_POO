import reflex as rx

from sistema_votaciones_POO.Backend.DB import User, Votos
from sistema_votaciones_POO.Backend.usuario import QueryUser


class candidatos(rx.Base):
    id: int
    nombre: str
    imagen: str
    partido: str
    genero: str
    edad: int
    costo_campaña: int
    cant_votos: int
    pvotos: float

class votaciones(rx.State):
    candidaturas: list[candidatos] = [
        candidatos(id=1, nombre="Stalin", imagen="/stalin.png", partido="Comunista", genero="Hombre", edad=40, costo_campaña=0, cant_votos=0, pvotos=0),
        candidatos(id=2, nombre="Hitler", imagen="/fuhrer.png", partido="Nazi", genero="Hombre", edad=45, costo_campaña=0, cant_votos=0, pvotos=0),
        candidatos(id=3, nombre="El Bicho", imagen="/bicho.png", partido="SIUUUU", genero="Hombre", edad=38, costo_campaña=0, cant_votos=0, pvotos=0),
        candidatos(id=4, nombre="Mao Zedong", imagen="/mao.png", partido="Comunista(China)", genero="Hombre", edad=60, costo_campaña=0, cant_votos=0, pvotos=0)
    ]
    
    cand: int = None
    medio_comunicacion: str = "Television"
    votos: list[Votos] = []

    @rx.var
    def totalVotos(self) -> int:
        with rx.session() as session:
            self.votos = session.exec(Votos.select().where(True)).all()
        return len(self.votos)
    
    def setVotosCandidato(self):
        votos = self.totalVotos
        for i, candidato in enumerate(self.candidaturas):
            votosC = 0
            costoC = 0
            for voto in self.votos:
                if voto.id_candidato == candidato.id:
                    votosC += 1
                    if voto.medio_comunicacion == "Television":
                        costoC += 1000
                    elif voto.medio_comunicacion == "Radio":
                        costoC += 500
                    elif voto.medio_comunicacion == "Internet":
                        costoC += 100
            candidato.cant_votos = votosC
            candidato.costo_campaña = costoC
            candidato.pvotos = round((votosC / (votos + 0.0000000001)) * 100, 2)

    def votar(self):
        try:
            with rx.session() as session:
                session.add(Votos(id_candidato=self.cand, medio_comunicacion=self.medio_comunicacion))
                session.commit()
            self.setVotosCandidato()
            self.sortCandidaturas()
        except Exception as e:
            print(f"Error al votar: {e}")

    def setCandidato(self, id):
        self.cand = id

    def sortCandidaturas(self):
            for l in range(0, 4):
                for i in range(1, 4):
                    if(self.candidaturas[i].cant_votos > self.candidaturas[i - 1].cant_votos):
                        candidatoAux = self.candidaturas[i]
                        self.candidaturas[i] = self.candidaturas[i - 1]
                        self.candidaturas[i - 1] = candidatoAux

    def vaciarUrna(self):
        try:
            with rx.session() as session:
                votos = session.exec(Votos.select().where(True)).all()
                for voto in votos:
                    session.delete(voto)
                session.commit()
                for candidato in self.candidaturas:
                    candidato.cant_votos = 0
                    candidato.costo_campaña = 0
                    candidato.pvotos = 0
        except Exception as e:
            print(f"Error al vaciar la urna: {e}")
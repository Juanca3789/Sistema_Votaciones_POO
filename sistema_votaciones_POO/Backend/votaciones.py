import reflex as rx

from sistema_votaciones_POO.Backend.DB import Votos


class candidatos(rx.Base):
        id: int
        nombre: str
        imagen: str
        partido: str
        genero: str
        edad: int
        costo_campaña: int
        cant_votos: str
        pvotos: float

class votaciones(rx.State):

    candidaturas : list[candidatos] = [
        candidatos(id= 1, nombre= "Stalin", imagen= "/stalin.png", partido= "Comunista", genero= "Hombre", edad= 40, costo_campaña= 0, cant_votos= 0, pvotos= 0),
        candidatos(id= 2, nombre= "Hitler", imagen= "/fuhrer.png", partido= "Nazi", genero= "Hombre", edad= 45, costo_campaña= 0, cant_votos= 0, pvotos= 0),
        candidatos(id= 3, nombre= "El Bicho", imagen= "/bicho.png", partido= "SIUUUU", genero= "Hombre", edad= 38, costo_campaña= 0, cant_votos= 0, pvotos= 0),
        candidatos(id= 4, nombre= "Mao Zedong", imagen= "/mao.png", partido= "Comunista(China)", genero= "Hombre", edad= 60, costo_campaña= 0, cant_votos= 0, pvotos= 0)
        ]
    
    cand : int
    medio_comunicacion: str
    votos: list[Votos]

    @rx.var
    def totalVotos(self) -> int:
        with rx.session() as session:
            self.votos = session.exec(
                Votos.select.where(True)
            ).all()
        contador = 0
        for voto in self.votos:
            contador += 1
        rx.console_log(contador)
        return contador
    
    def setVotosCandidato(self):
        votos = self.totalVotos
        for i in range(0, 4):
            votosC = 0
            costoC = 0
            for voto in self.votos:
                if(voto.id_candidato == i + 1):
                    votosC += 1
                    if(voto.medio_comunicacion == "Television"):
                        costoC += 1000
                    elif(voto.medio_comunicacion == "Radio"):
                        costoC += 500
                    elif(voto.medio_comunicacion == "Internet"):
                        costoC += 100
            self.candidaturas[i].cant_votos = votosC
            self.candidaturas[i].costo_campaña = costoC
            self.candidaturas[i].pvotos = round((votosC/(votos + 0.0000000001)) * 100)

    def votar(self):
        with rx.session() as session:
            session.add(
                Votos(
                    id_candidato= self.cand,
                    medio_comunicacion= self.medio_comunicacion
                )
            )
            session.commit()
        self.setVotosCandidato()

    def setCandidato(self, id):
        self.cand = id
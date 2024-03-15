import reflex as rx

from sistema_votaciones_POO.Backend.DB import User


class QueryUser(rx.State):
    nombre: str
    num_cedula: int
    clave: str
    users: list[User]
    aux1: bool = False
    aux2: bool = False

    def iniciarSesion(self) -> bool:
        with rx.session() as session:
            self.users = session.exec(
                User.select.where(
                    (User.num_cedula == self.num_cedula) & (User.clave == self.clave)
                )
            ).all()
            if(self.users):
                self.users[0].nombre = self.users[0].nombre.capitalize()
                self.aux1 = True
            else:
                self.aux1 = False
    
    def nuevoUsuario(self) -> bool:
        with rx.session() as session:
            self.users = session.exec(
                User.select.where(
                    User.num_cedula == self.num_cedula
                )
            ).all()
            if(self.users):
                self.aux2 = False
            else:
                session.add(
                    User(nombre= self.nombre, num_cedula= self.num_cedula, clave= self.clave)
                )
                session.commit()
                self.aux2 = True
    
    def onReg(self):
        self.aux2 = False
    
    def cerrarSesion(self):
        self.aux1 = False
        self.nombre = ""
        self.num_cedula = 0
        self.clave = ""
        self.users.clear()
        rx.redirect(
            "/"
        )
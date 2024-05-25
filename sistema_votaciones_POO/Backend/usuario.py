import re

import reflex as rx

from sistema_votaciones_POO.Backend.DB import User, Votos


class QueryUser(rx.State):
    nombre: str
    num_cedula: int
    clave: str
    users: list[User]
    aux1: bool = False
    aux2: bool = False
    current_user_id: int = 0

    def iniciarSesion(self) -> bool:
        with rx.session() as session:
            self.users = session.exec(User.select().where((User.num_cedula == self.num_cedula) & (User.clave == self.clave))).all()
            if self.users:
                self.users[0].nombre = self.users[0].nombre.capitalize()
                self.aux1 = True
                self.set_current_user_id(self.users[0].id)
            else:
                self.aux1 = False

    def nuevoUsuario(self) -> bool:
        if not re.match("^[a-zA-Z\s]+$", self.nombre):
            raise Exception("El nombre no puede contener números")
        if not re.match("^\d+$", str(self.num_cedula)):
            raise Exception("El número de cédula no puede contener letras")
        if len(self.clave) < 8:
            raise Exception("La contraseña debe tener al menos 8 caracteres")
        with rx.session() as session:
            self.users = session.exec(User.select().where(User.num_cedula == self.num_cedula)).all()
            if self.users:
                self.aux2 = False
            else:
                session.add(User(nombre=self.nombre, num_cedula=self.num_cedula, clave=self.clave, ha_votado= False))
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
        self.current_user_id = 0
        rx.redirect("/")

    def set_current_user_id(self, user_id: int):
        self.current_user_id = user_id

    def get_current_user_id(self) -> int:
        return self.current_user_id

    def clear_current_user_id(self):
        self.current_user_id = 0

    def validar_nombre(self, nombre: str) -> bool:
        return re.match("^[A-Za-z ]+$", nombre) is not None

    def validar_cedula(self, num_cedula: int) -> bool:
        return re.match("^[0-9]+$", str(num_cedula)) is not None

    def validar_clave(self, clave: str) -> bool:
        return len(clave) >= 8
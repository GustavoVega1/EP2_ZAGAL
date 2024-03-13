from modulos import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(45), nullable = False)
    destino = db.Column(db.String(45), nullable = False)
    mensaje = db.Column(db.String(45), nullable = False)

    def __init__(self, nombre, destino, mensaje):
        self.nombre = nombre
        self.destino = destino
        self.mensaje = mensaje
    
    def __repr__(self ):
        return f'<User{self.destino}<'
from mongoengine import *

#crear la clase que representa la coleccion genero en la base de datos

class Genero(Document):
    nombre= StringField(max_length=50, unique=True,required=True)
    
    def __repr__(self):
        return self.nombre
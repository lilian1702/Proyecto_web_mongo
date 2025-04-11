from mongoengine import *

class Usuario(Document):
    usuario= StringField(max_length=50, unique=True,required=True)
    password= StringField(max_length=50, unique=True,required=True)
    nombres= StringField(max_length=50, unique=True,required=True)
    apellidos= StringField(max_length=50, unique=True,required=True)
    correo= StringField(max_length=50, unique=True,required=True)
    
    def __repr__(self):
        return f"{self.nombres}, {self.apellidos}"
    

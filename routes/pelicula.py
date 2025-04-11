from app import app
from flask import  Flask, request, render_template
from models.pelicula import Pelicula
from models.genero import Genero
from bson.objectid import ObjectId

@app.route("/pelicula/", methods=['GET'])
def listapelicula():
    try:
        mensaje=None
        peliculas=Pelicula.objects()
    except Exception as error:
        mensaje=str(error)
        
    return{"mensaje":mensaje, "pelicula":peliculas}

@app.route("/pelicula/", methods=['POST'])
def addPelicula():
    try:
        mensaje= None
        estado= False
        if request.method=='POST':
            datos=request.get_json(force=True)
            genero=Genero.objects(id=datos['genero']).first()
            if genero is None:
                mensaje="genero no existe, no se puede crear la pelicula"            
           
            else:
                datos['genero']=genero
                pelicula= Pelicula(**datos)
                pelicula.save()
                estado=True
                mensaje="Pelicula agregado correctamente"
        else:
            mensaje="no permitido"
        
    except Exception as error:
        mensaje=str(error)
        
    return{"estado":estado, "mensaje":mensaje}


@app.route("/pelicula/", methods=['PUT'])
def updatePelicula():
    try:
        mensaje= None
        estado= False
        if request.method=='PUT':
            datos=request.get_json(force=True)
            #obtener pelicula por id 
            pelicula=Pelicula.objects(id=datos['id']).first()
            #actualizar sus atributos
            pelicula.codigo= datos['codigo']
            pelicula.titulo= datos['titulo']
            pelicula.protagonista= datos['protagonista']
            pelicula.resumen= datos['resumen']
            pelicula.foto= datos['foto']
            genero=Genero.objects(id=datos['genero']).first()
            if genero is None:
                mensaje="no se actualiza el genero."
            else:
                pelicula.genero=genero
            pelicula.save()
            mensaje =f"{mensaje} pelicula actualizada" 
            estado=True
        else: 
            mensaje="no permitido"
    except Exception as error:
        mensaje=str(error)
        
    return{"estado":estado, "mensaje":mensaje}

    
            
@app.route("/peliculas/", methods=['GET'])
def listarpeliculas():    
    peliculas=Pelicula.objects()
    generos=Genero.objects()        
    return render_template("listarpeliculas.html",peliculas=peliculas,generos=generos)          
            
            
    
@app.route("/agregarPelicula/",methods=["GET"])
def AgregarPelicula():
    generos=Genero.objects()
    return render_template("frmAgregarPelicula.html", generos=generos)  


@app.route("/vistaEditarPelicula/<string:id>/",methods=['GET'])
def mostrarVistaEditarPelicula(id):
    peliculas=Pelicula.objects(id=ObjectId(id)).first()
    generos=Genero.objects()    
    return render_template("frmEditarPelicula.html", peliculas=peliculas, generos=generos)
    
 

@app.route("/pelicula/", methods=['DELETE'])
def deletePelicula():
    try:
        mensaje = None
        estado = True
        if request.method == "DELETE":
            datos = request.get_json(force=True)
            pelicula = Pelicula.objects(id=datos['id']).first()
            if (pelicula is None):
                mensaje = "No es posible eliminar pelicula con ese id"
            else:
                pelicula.delete()
                estado = True
                mensaje = "Película Eliminada correctamente"
        else:
            mensaje = "No permitido"
    except Exception as error:
        mensaje = str(error)

    return {"estado": estado, "mensaje": mensaje}

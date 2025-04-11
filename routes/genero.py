from flask import request, render_template
from models.genero import Genero
from app import app
from models.pelicula import Pelicula
from bson.objectid import ObjectId

@app.route("/genero/", methods=['GET'])
def listarGeneros():
    
    """_summary_
        funcion que retorno la lsita de generos
        exixtentes en la coleccion generos
    Returs:
        _type_: lista de generos      
    
    """
    try:
        mensaje=None
        generos= Genero.objects()
        
    except Exception as error:
        mensaje=str(error)
        
    
    return{"mensaje": mensaje, "generos":generos}


@app.route("/genero/",methods=["POST"])
def addGenero():
    try:
        mensaje=None
        estado= False
        if request.method=="POST":
            datos= request.get_json(force=True)
            genero=Genero(**datos)
            genero.save()            
            estado=True
            mensaje="producto agregado correctamente"
        else:
            mensaje="tarea no permitida"
            
    except Exception as error:
        mensaje=str(error)
        
    return {"estado":estado,"mensaje":mensaje}


@app.route("/genero/", methods=["PUT"])
def updateGenero():
    try:
        mensaje=None
        estado=False
        if request.method=='PUT':
            datos=request.get_json(force=True)
            genero = Genero.objects(id=datos['id']).first()
            genero.nombre=datos['nombre']
            genero.save()
            mensaje="genero actualizado"
            estado=True       
            
        else:
            mensaje="no permitido"
    except Exception as error:
        mensaje=str(error)
        
    return {"estado": estado, "mensaje":mensaje}

@app.route("/genero/", methods=["DELETE"])
def deleteGenero():
    try:
        mensaje=None
        estado=False
        if request.method=='DELETE':
            datos=request.get_json(force=True)
            genero = Genero.objects(id=datos['id']).first()
            peliculas=Pelicula.objects()
            if(len(peliculas)>0):
                mensaje= "no se puede eliminar, no permitido"
            else:
                if genero is None:
                    mensaje="genero no encontrado. no se puede eliminar"
                else:
                    genero.delete()
                    estado=True
                    mensaje="genero eleminado"
        else:
            mensaje="no permitido"
    except Exception as error:
        mensaje=str(error)
    
    return {"estado": estado, "mensaje":mensaje}



# @app.route("/generos", methods=['GET'])
# def listarGeneros():
#     try:    
#         generos=Genero.objects()
#         return render_template("listarGeneros.html", generos=generos)
#     except Exception as error:
#         mensaje=str(error)
#         return render_template("listarGeneros.html",generos=None, mensaje=mensaje)

@app.route("/generos/", methods=["GET"])

def listarGenero():
    try:
        mensaje=""
        generos=Genero.objects()
    except Exception as error:
        mensaje=str(error)
    
    return render_template("listarGeneros.html",
                           generos=generos,mensaje=mensaje)       
        

@app.route("/vistaGenero/")
def agregarGenero():
    return render_template("frmAgregarGenero.html")

@app.route("/editarGenero/<id>", methods=["GET"])
def editarGenero(id):
    try:
        mensaje=" "
        genero=Genero.objects(id=ObjectId(id)).first()
        print(genero)
    except Exception as error:
        mensaje=str(error)
    return render_template("frmEditarGeneros.html",genero=genero, mensaje=mensaje)
from app import app,db,recaptcha
from flask import Flask, request, render_template, session
from models.usuario import Usuario
import yagmail
import threading
from dotenv import load_dotenv
import os

load_dotenv()


@app.route("/")
def login():
    return render_template("frmIniciarSesion.html")

@app.route("/usuario/",methods=["GET"])
def listarUsuario():
    try:
        mensaje=None
        usuarios=Usuario.objects()
    except Exception as error:
        mensaje=str(error)
    return {"mensaje": mensaje,"usuarios": usuarios}

@app.route("/home/")
def home():
    return render_template("contenido.html")

@app.route("/iniciarSesion/",methods=["POST"])
def iniciarSesion():
    mensaje=None
    try:
        if request.method=='POST':
            if recaptcha.verify():
                print("SUCCESS")
            else:
                print("FAILED")
            username = request.form['txtUser']
            password = request.form['txtPassword']

            usuario=Usuario.objects(usuario=username,password=password).first()
            correo=os.environ.get("CORREO")
            clave=os.environ.get("ENVIAR_CORREO")
            if usuario:
                session['user']=username
                session['user_name']=f"{usuario.nombres} {usuario.apellidos}"
                email= yagmail.SMTP(correo,clave, encoding="utf-8")
                asunto="Ingreso al sistema"
                mensaje=f"ha ingresado al aplicativo {usuario.nombres} {usuario.apellidos}"
                thread=threading.Thread(target=enviarCorreo, args=(email, [usuario.correo], asunto,mensaje))
                thread.start()
                return render_template("contenido.html")
            else:
                mensaje="credenciales incorrectas"
    except Exception as error:
        mensaje=str(error)

    return render_template("frmIniciarSesion.html", mensaje=mensaje)
def enviarCorreo(email=None, destinatario=None, asunto=None, mensaje=None):
   email.send(to=destinatario, subject=asunto, contents=mensaje)
    
@app.route("/cerrarSesion/")
def cerrarSesion():
    session.clear()
    mensaje="sesion cerrada"
    return render_template("frmIniciarSesion.html", mensaje=mensaje)
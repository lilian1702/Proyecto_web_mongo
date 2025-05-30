from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from dotenv import load_dotenv
import os   
from google_recaptcha_flask import ReCaptcha


load_dotenv()  # Esto carga las variables del .env al entorno


app = Flask(__name__) 
app.secret_key="adsocauca"


uri=os.environ.get("URI")
db=os.environ.get("DB")
app.config["UPLOAD_FOLDER"] = "./static/imagenes"
app.config["MONGODB_SETTINGS"] = [{
    "db":db,
    "host":uri,
    #"port": 27017
}]
# Configuración de Google ReCaptcha
app.config.update(dict(
     GOOGLE_RECAPTCHA_ENABLED=True,    
    GOOGLE_RECAPTCHA_SITE_KEY=os.environ.get("CLAVE_SITIO"),
    GOOGLE_RECAPTCHA_SECRET_KEY=os.environ.get("CLAVE_SECRETA"),
    
   
))

db=MongoEngine(app)
recaptcha=ReCaptcha(app)
from routes.genero import *
from routes.pelicula import *
from routes.usuario import *



if __name__=="__main__":
    
   
    app.run(port=3000, host="0.0.0.0",debug=True)
    
    
    


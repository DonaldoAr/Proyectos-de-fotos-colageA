from flask import *
from flask_cors import CORS, cross_origin
import base64
import requests
import json
import re
app = Flask(__name__)
cors = CORS(app)
from colageImg import opacidadImagenes
# PATHS
# PathImagOri = r"./MosaicoPython/public/rel"
PathImagOri = r"./static/uploads"
PathImagenesRe = r"./public/Img"
PathImagenAgua = r"./fondo.jpg"
UPLOAD_FOLDER = 'static/uploads'

contador = 0
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/img',methods=['POST'])
@cross_origin()
def img():
    global contador
    image_64_decode = base64.decodebytes(request.data) 
    contador += 1
    image_result = open(UPLOAD_FOLDER+str(contador)+'.jpg', 'wb')
    image_result.write(image_64_decode)
    opacidadImagenes(PathImagOri, PathImagenesRe, PathImagenAgua, contador)
   #  return redirect(request.url/)
    return redirect('index.html')
   #  return "exito"

# PARA MOSTRAR LA IMAGEN
@app.route('/display')
def display_image():
    return render_template('index2.html')

# RUTA NO ENCONTRADA
@app.errorhandler(404)
def not_found(error = None):
    response = jsonify({
        'message': 'Dato no encontrado :( ' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000, debug=True)
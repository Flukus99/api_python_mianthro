from flask import Flask,jsonify,request,send_from_directory
from ia_unica import ia_funcional
from ia_multi import llamar
import json
from os import getcwd,remove,path
from flask_cors import CORS


PATH_FILE=getcwd()+"/files/"
PATH_FILE2=getcwd()
app= Flask(__name__)

CORS(app)

@app.route('/')
def index():
    return 'el servidor esta funcionando'


@app.route('/unico',methods=["POST"])
def hello():
    peso=request.json['peso']
    talla=request.json['talla']
    genero=request.json['genero']
    resultado=int(ia_funcional(peso,talla,genero))
    try:
        return jsonify({"resultado":resultado})
    except:
        return jsonify({"error":"algo salio mal"})    
    

@app.route('/multi/<string:token>', methods=["POST"])
def hacer_multi(token):
    archivo=request.files["file"]
    url=PATH_FILE + token +".xlsx"
    archivo.save(url)

    llamar(url,token)
    try:
        return send_from_directory(PATH_FILE2,token+".json",as_attachment=True)
    except:
        return jsonify({"error":"Aalgo salio mal, Revisa el documento y sus columnas"})  

@app.route('/multi_delete/<string:token>', methods=["DELETE"])
def delete_data(token):
    if path.isfile(PATH_FILE + token +".xlsx")==False:
        return jsonify({"errror":"File does not exist"})
    elif path.isfile(PATH_FILE2 +"/"+ token+".json")==False:
        return jsonify({"errror":"File does not exist"})
    else:
        remove(PATH_FILE + token +".xlsx")
        remove(PATH_FILE2 +"/"+ token+".json")
        return("archivos eliminados con exito")

    


if __name__=='__main__':
    app.run(debug=False, host="0.0.0.0")












from flask import Flask,jsonify,request
from ia_unica import ia_funcional
from ia_multi import llamar
import json
from os import getcwd


PATH_FILE=getcwd()+"/files/"

app= Flask(__name__)

@app.route('/unico')
def hello():
    resultado=int(ia_funcional(4,55,"nino"))
    return jsonify({"resultado":resultado})
    



@app.route('/multi', methods=["POST"])
def hacer_multi():
    archivo=request.files["file"]
    archivo.save(PATH_FILE + archivo.filename)

    
    return "se ejecuto"



if __name__=='__main__':
    app.run(debug=True, port=4000)












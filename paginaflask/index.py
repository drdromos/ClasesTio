from flask import Flask , render_template , request , redirect , url_for
app = Flask(__name__)

@app.route("/")
def hello():
     return render_template('index.html')

@app.route("/login")
def login():    
    return render_template('otro.html')

@app.route("/signup" , methods=["POST" , "GET"])
def signup():    
    if request.method == "POST":
        fullname = request.form['fullname']
        celular = request.form['phone']
        edad = request.form['age']
        return render_template('signup.html' , nombre=fullname , telefono=celular , vejez=edad)
    else:
        return "algo está mal"
    return render_template('signup.html')

@app.route("/detalle/<string:name>/<string:health>/<string:food>/<string:personality>" , methods=["GET"])
def detalle(name:str , health:str , food:str , personality:str):
    if request.method == "GET":
        return render_template('detalle.html' , nombre=name , salud=health , alimento=food , personalidad=personality)

if __name__ == "__main__":   
    app.run(host='0.0.0.0')
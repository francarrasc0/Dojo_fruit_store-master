from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    nombre_usuario = request.form['first_name'] + " " + request.form['last_name'] 
    frutas = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    if frutas == 1:
        print (f'Cobrando a {nombre_usuario} por {frutas} fruta')
    elif (frutas > 0):
        print (f'Cobrando a {nombre_usuario} por {frutas} frutas')
    else :
        print ('No hay frutas que cobrar')    
    return render_template("checkout.html", form = request.form)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    
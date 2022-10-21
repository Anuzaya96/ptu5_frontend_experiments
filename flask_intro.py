from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Veikia!"

# Sukuriam kita puslapi

@app.route("/sveikas/<name>")
def user(name):
    return f"Sveikas, {name}"

@app.route("/grazi_diena")
def grazi_diena():
    return render_template("grazi_diena.html")

@app.route("/zmones")
def zmones():
    zmones = [
        'Justina', 'Darius', 'Ingrida', 'Linas',
        'Ana', 'Simas', 'Arnoldas', 'Sergejus'
    ]
    return render_template("zmones.html", zmones=zmones)

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/hello")
def hello():
    return render_template("hello.html", **request.args)

if __name__ == "__main__":
    app.run(debug=True)

#iniciar las librerías
from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "server local, listo! hola"

if __name__ == "__main__":
    app.run(debug=True)
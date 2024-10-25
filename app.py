from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hola():
    mensaje = "HOLA"  # Aquí defines la variable que quieres pasar al HTML
    return render_template('index.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/leer')
def leer():
    try:
        result = subprocess.run(['python3', 'leer.py'], capture_output=True, text=True)
        datos = result.stdout
    except Exception as e:
        datos = f"Error al ejecutar leer.py: {str(e)}"
    return render_template('index.html', mensaje=datos)

@app.route('/insertar')
def insertar():
    try:
        result = subprocess.run(['python3', 'insertar.py'], capture_output=True, text=True)
        datos = result.stdout
    except Exception as e:
        datos = f"Error al ejecutar insertar.py: {str(e)}"
    return render_template('index.html', mensaje=datos)

if __name__ == '__main__':
    app.run(debug=True)

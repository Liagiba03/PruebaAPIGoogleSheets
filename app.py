from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def mostrar_datos():
    try:
        # Ejecuta `leer.py` y captura su salida
        result = subprocess.run(['python3', 'leer.py'], capture_output=True, text=True)
        datos = result.stdout  # Captura la salida del script
    except Exception as e:
        datos = f"Error al ejecutar leer.py: {str(e)}"

    # Pasar los datos al HTML
    return render_template('index.html', mensaje=datos)

if __name__ == '__main__':
    app.run(debug=True)

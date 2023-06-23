from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    # Realizar una solicitud GET a la API de Dailymotion para obtener datos
    dataImport = requests.get('https://api.dailymotion.com/videos?channel=sport&limit=10')
    
    # Convertir la respuesta JSON en un objeto Python
    dataImportJSON = dataImport.json()
    
    # Imprimir los datos importados en la consola
    print(dataImportJSON)
    
    # Renderizar la plantilla 'index.html' y pasar los datos a la plantilla
    return render_template('index.html', data=dataImportJSON['list'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 
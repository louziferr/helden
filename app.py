from flask import Flask, render_template
import json

# App erstellen
app = Flask(__name__)

# Daten einlesen
with open('static/helden.json') as f:
    helden = json.load(f)['charaktere']

@app.route('/')
def index():
    return render_template('index.html', helden=helden)

# App starten
app.run(debug=True)
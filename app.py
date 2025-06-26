from flask import Flask, render_template, request
import model

# App erstellen
app = Flask(__name__)

# Daten einlesen
helden = model.daten_einlesen()

@app.route('/')
def index():
    return render_template('index.html', helden=helden)

@app.route('/held')
def held():
    id = request.args.get('id')

    if id: id = int(id)
    else: return "No ID"

    # Helden mit der ID raussuchen
    gefunden = False
    for held in helden:
        if id == held['id']:
            gefunden = True
            break

    if gefunden:
        return render_template('held.html', held=held)
    return 'Not Found'

# App starten
app.run(debug=True)
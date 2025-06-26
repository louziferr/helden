'''Model-Funktionen für die Helden-Website'''
import json

def daten_einlesen(datei='static/helden.json'):
    # Daten einlesen
    with open(datei) as f:
        helden = json.load(f)['charaktere']
    return helden
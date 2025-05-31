import os
import sys
import logging
import logging.config
from flask import Flask, render_template, request, abort
import flask_monitoringdashboard as dashboard
import yaml

# Initialisation des logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log", mode='a', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

# Définition du répertoire racine
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
template_dir = os.path.join(base_dir, 'templates')
index_file = os.path.join(template_dir, 'index.html')

# Vérification des chemins
if not os.path.isdir(template_dir):
    logging.error(
        "❌ Dossier 'templates' introuvable à l’emplacement : %s",
        template_dir
    )
    sys.exit(1)

if not os.path.isfile(index_file):
    logging.error("❌ Fichier 'index.html' introuvable dans : %s", template_dir)
    sys.exit(1)

# Création de l'app Flask
app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def home():
    """Page d'accueil"""
    logging.info("✅ Route / appelée avec succès")
    return render_template('index.html')


if __name__ == '__main__':
    logging.info(
        "🚀 Démarrage du serveur Flask avec les templates : %s",
        template_dir
    )
    app.run(debug=True)


@app.before_request
def block_curl_user_agent():
    if "curl" in request.headers.get("User-Agent", ""):
        abort(403)

dashboard.bind(app)
dashboard.bind(app)

with open('logging_config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
    logging.config.dictConfig(config)

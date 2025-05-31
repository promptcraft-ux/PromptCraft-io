import os
import yaml
import logging.config
from flask import request, jsonify
from app import app


def test_home_route():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"PromptCraft" in response.data


def test_favicon_route():
    tester = app.test_client()
    response = tester.get('/favicon.ico')
    assert response.status_code in [200, 404]  # favicon optionnel


def test_404_route():
    tester = app.test_client()
    response = tester.get('/page-inexistante')
    assert response.status_code == 404


def setup_logging(config_path="config/logging_config.yaml"):
    if not os.path.exists(config_path):
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        default_config = """
version: 1
formatters:
  default:
    format: "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
handlers:
  rotating_file_handler:
    class: logging.handlers.RotatingFileHandler
    level: INFO
    formatter: default
    filename: logs/app.log
    maxBytes: 1000000
    backupCount: 5
root:
  level: INFO
  handlers: [rotating_file_handler]
"""
        with open(config_path, "w") as f:
            f.write(default_config)

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
        logging.config.dictConfig(config)


# Initialisation Flask
setup_logging()
# app is already imported from the main app module;
# no need to redefine it here.


@app.route("/test-log")
def test_log():
    app.logger.info(
        "✅ Ceci est un test manuel de log depuis la route /test-log."
    )
    return "Log généré avec succès !"


@app.before_request
def security_middleware():
    if request.endpoint != 'static' and "X-Auth-Token" not in request.headers:
        app.logger.warning(f"❌ Requête non autorisée vers {request.path}")
        return jsonify({"error": "Access denied"}), 403
        return jsonify({"error": "Access denied"}), 403

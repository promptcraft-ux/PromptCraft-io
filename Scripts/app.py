# Script Flask minimal pour serveur local
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Bienvenue sur PromptCraft!'

if __name__ == '__main__':
    app.run(debug=True)
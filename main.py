from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Folder do przechowywania wczytanych zdjęć
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def upload_file():
    return render_template('upload.html')


@app.route('/predict', methods=['POST'])
def predict():

        return 'Predykcja marki samochodu: ...'  # Zwróć wynik predykcji


if __name__ == '__main__':
    app.run(debug=True)
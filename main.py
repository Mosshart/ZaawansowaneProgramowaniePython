from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from PIL import Image
import json

app = Flask(__name__)

# Folder do przechowywania wczytanych zdjęć
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
MODEL_URL = 'https://tfhub.dev/google/imagenet/mobilenet_v2_130_224/classification/4'
model = tf.keras.Sequential([hub.KerasLayer(MODEL_URL, input_shape=(224, 224, 3))])
model.build([None, 224, 224, 3])

with open('imagenet_class_index.json') as f:
    labels = json.load(f)
def class_id_to_label(i):
    return labels[i]
def load_and_prepare_image(image_path):
    img = Image.open(image_path).resize((224, 224))
    img = np.array(img) / 255.0
    img = img[np.newaxis, ...]
    return img


@app.route('/')
def upload_file():
    return render_template('upload.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(file_path)

        # predykcja
        img = load_and_prepare_image(file_path)
        predictions = model.predict(img)
        predicted_class = np.argmax(predictions, axis=-1)
        predicted_label = class_id_to_label(predicted_class[0] - 1)

        return render_template('predict.html', filename=filename, predicted_label=predicted_label)


if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(host="0.0.0.0", port=5000)
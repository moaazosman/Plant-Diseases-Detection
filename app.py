from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import tensorflow as tf
import time

# Define the models and their respective class labels
models = {
    'tomato': {
        'model_file': 'tomato_disease_model_4.h5',
        'class_labels': ['Healthy', 'Infected: Bacterial Spot', 'Infected: Early Blight',
                         'Infected: Late Blight', 'Infected: Leaf Curl Virus', 'Infected: Leaf Mold',
                         'Infected: Mosaic Virus', 'Infected: Septoria Leaf Spot', 'Infected: Spider Mites',
                         'Infected: Target Spot']
    },
    'grape': {
        'model_file': 'Grape_disease_detection_2.h5',
        'class_labels': ['Healthy', 'Infected with Black Rot', 'Infected with Esca', 'Infected with Leaf Blight']
    },
    'corn': {
        'model_file': 'corn_disease_detection_model2.h5',
        'class_labels': ['Healthy', 'Infected with Common Rustt','Infected with Gray Leaf Spot', 'Infected with Northern Leaf Blight']
    },
    'potato': {
        'model_file': 'potato_disease_model1.h5',
        'class_labels': ['Healthy', 'Infected by Early Blight', 'Infected by Late Blight']
    }
}

# Create a Flask application
app = Flask(__name__, static_folder='static')

# Define the main route
@app.route('/', methods=['GET', 'POST'])
def upload_predict():
    if request.method == 'POST':
        # Get the uploaded image file and selected model
        image_file = request.files['image']
        model_name = request.form['model']

        if image_file:
            # Open and preprocess the image
            img = Image.open(image_file)
            img = img.resize((64, 64))  # Resize the image to match the model's input size
            img = np.array(img) / 255.0
            img = np.expand_dims(img, axis=0)

            # Show loading circle
            time.sleep(0.5)  # Simulating prediction delay

            # Perform the prediction
            predicted_class = predict_image(model_name, img)

            # Render the template with the result and image filename
            return render_template('index.html', result=predicted_class, image_file=image_file.filename)

    # Render the template without any result or image filename
    return render_template('index.html')

def predict_image(model_name, img):
    model_file = models[model_name]['model_file']
    class_labels = models[model_name]['class_labels']
    
    # Load the machine learning model
    model = tf.keras.models.load_model(model_file)

    # Perform the prediction
    prediction = model.predict(img)
    predicted_class_index = np.argmax(prediction)
    predicted_class = class_labels[predicted_class_index]
    
    return predicted_class

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

import numpy as np 
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline: 
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # load model
        model = load_model(os.path.join("model", "model.h5"))

        imagename = self.filename  # Get the image filename
        test_image = image.load_img(imagename, target_size=(224, 224))  # Load and resize the image
        test_image = image.img_to_array(test_image)  # Convert the image to array
        test_image = np.expand_dims(test_image, axis=0)  # Expand dimensions to match model input shape
        result = np.argmax(model.predict(test_image), axis=1)  # Predict the class label
        print(result)  # Print the predicted class label

        if result[0] == 1:
            prediction = 'Tumor'
            return [{ "image" : prediction}]
        else:
            prediction = 'Normal'
            return [{ "image" : prediction}]
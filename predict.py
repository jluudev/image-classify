from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import logging

os.environ['CURL_CA_BUNDLE'] = ""

# Initialize the Blueprint
bp = Blueprint('predict', __name__, url_prefix='/predict')

# Set up the pre-trained model
model = ResNet50(weights='imagenet')

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@bp.route('/', methods=['POST'])
def predict():
    # Check if the post request has the file part
    if 'image' not in request.files:
        logger.error('No image part in the request')
        return jsonify({'error': 'No image part in the request'}), 400

    file = request.files['image']

    # If user does not select file, the browser submits an empty file without a filename
    if file.filename == '':
        logger.error('No image selected for uploading')
        return jsonify({'error': 'No image selected for uploading'}), 400

    try:
        # Secure the filename to avoid unsafe paths and save the file temporarily
        filename = secure_filename(file.filename)
        temp_file_path = os.path.join('/tmp', filename)
        file.save(temp_file_path)

        # Load and preprocess the image
        img = image.load_img(temp_file_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array_expanded_dims = np.expand_dims(img_array, axis=0)
        processed_image = preprocess_input(img_array_expanded_dims)

        # Make prediction
        predictions = model.predict(processed_image)
        results = decode_predictions(predictions, top=3)[0]

        # Clean up the temporary file
        os.remove(temp_file_path)

        # Format the results and prepare the JSON response
        prediction_data = [{'label': label, 'probability': float(prob)} for _, label, prob in results]

        logger.info('Image successfully processed')
        return jsonify(prediction_data)
        
    except Exception as e:
        logger.error('Error processing image', exc_info=True)
        return jsonify({'error': 'Error processing image', 'message': str(e)}), 500

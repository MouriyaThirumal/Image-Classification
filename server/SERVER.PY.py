from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import io
from PIL import Image
import util  # Assuming util.py contains your classification model code

app = Flask(__name__)
CORS(app)  # Enables Cross-Origin Resource Sharing (CORS)


# Define your route with GET and/or POST methods as required
@app.route('/classify_image', methods=['POST'])
def classify_image():
    if request.method == 'POST':
        # Get the base64 image data from the request
        image_data = request.form['image_data']

        # Strip the prefix (if any) like "data:image/png;base64,"
        if image_data.startswith('data:image'):
            image_data = image_data.split(",")[1]

        # Decode the base64 string to bytes
        image_bytes = base64.b64decode(image_data)

        # Convert bytes to image
        image = Image.open(io.BytesIO(image_bytes))

        # Call your utility function to classify the image
        result = util.classify_image(image)  # Modify this to handle the image directly if needed

        # Return the classification result as JSON
        response = jsonify(result)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()  # Assuming you load your model here
    app.run(port=5000)

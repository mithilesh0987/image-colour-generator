from flask import Flask, request, send_file, jsonify
from PIL import Image, ImageOps
import io
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

def colorize_image(image, style="vibrant"):
    """
    A placeholder colorization function that applies a basic color tint.
    Replace this with a real colorization model if available.
    """
    # Apply a basic color tint based on the style selected
    if style == "vibrant":
        colorized_image = ImageOps.colorize(image, black="blue", white="yellow")
    elif style == "pastel":
        colorized_image = ImageOps.colorize(image, black="lightblue", white="lightpink")
    elif style == "natural":
        colorized_image = ImageOps.colorize(image, black="green", white="brown")
    else:
        colorized_image = ImageOps.colorize(image, black="gray", white="white")

    return colorized_image.convert("RGB")  # Ensure RGB format for colorized output

@app.route("/colorize", methods=["POST"])
def colorize():
    try:
        # Get the uploaded file and style
        file = request.files.get("file")
        if file is None or file.filename == '':
            logging.error("No file provided in the request.")
            return jsonify({"error": "No file provided"}), 400
        
        style = request.form.get("style", "vibrant")

        # Open the image in grayscale mode
        image = Image.open(file).convert("L")

        # Apply colorization
        colorized_image = colorize_image(image, style)

        # Save colorized image to a byte buffer in JPEG format
        img_io = io.BytesIO()
        colorized_image.save(img_io, format="JPEG")
        img_io.seek(0)

        return send_file(img_io, mimetype="image/jpeg")

    except Exception as e:
        logging.error(f"Error during colorization: {e}")
        return jsonify({"error": "Failed to process image"}), 500

if __name__ == "__main__":
    app.run(debug=True)

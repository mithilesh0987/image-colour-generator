from flask import Flask, request, send_file
from PIL import Image
import io

app = Flask(__name__)

# Colorization function placeholder (replace with your model code)
def colorize_image(image, style="vibrant"):
    processed_image = image  # Replace with colorization logic
    return processed_image

@app.route("/colorize", methods=["POST"])
def colorize():
    file = request.files.get("file")
    style = request.form.get("style", "vibrant")
    image = Image.open(file).convert("L")
    colorized_image = colorize_image(image, style)
    img_io = io.BytesIO()
    colorized_image.save(img_io, format="JPEG")
    img_io.seek(0)
    return send_file(img_io, mimetype="image/jpeg")

if __name__ == "__main__":
    app.run(debug=True)

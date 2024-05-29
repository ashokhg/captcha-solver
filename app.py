from flask import Flask, request, render_template, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
import cv2
import numpy as np
import tensorflow as tf

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads/"
app.config["ALLOWED_EXTENSIONS"] = {"png", "jpg", "jpeg", "gif"}
app.secret_key = "We are all upgraded monkeys."

# loading my saved model at the start of the application
model = tf.keras.models.load_model("./main_dataset_model.h5")


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]
    )


def preprocess_image(image_path, target_size):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Image {image_path} not found.")
    img = cv2.resize(img, target_size)
    img = img / 255.0
    # img = img[..., np.newaxis]
    img = np.expand_dims(img, axis=0)
    return img


def predict_captcha(model, preprocessed_img):
    prediction = model.predict(preprocessed_img)
    predicted_label = "".join(
        [str(np.argmax(char_prob)) for char_prob in prediction[0]]
    )
    return predicted_label


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            print(filename, filepath, end="\n")

            try:
                preprocessed_img = preprocess_image(filepath, (190, 80))
                prediction = predict_captcha(model, preprocessed_img)
                return render_template(
                    "result.html", filename=filename, prediction=prediction
                )
            except Exception as e:
                flash(str(e))
                return redirect(request.url)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

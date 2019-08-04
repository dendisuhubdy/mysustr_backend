import redis
import pickle
import base64
from io import BytesIO
from PIL import Image
import numpy as np
import cv2
import jsonpickle
import os


from flask import Flask, render_template
from flask_restful import Resource, Api

CAMERA_FOLDER = os.path.join('static', 'camera')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = CAMERA_FOLDER
api = Api(app)

redis_image = redis.StrictRedis(host="localhost", port=6379, db=0)

@app.route('/')
@app.route('/index')
def show_index():
    b64 = redis_image.get("image")
    # b64 = b64.decode("utf-8")
    image = Image.open(BytesIO(base64.b64decode(b64)))
    image.save("./static/camera/temp.jpg")
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], "temp.jpg")
    # img = np.array(image)
    # print(img)
    del b64
    del image
    return render_template("index.html", user_image=full_filename)

if __name__ == '__main__':
    app.run(debug=True, port=5555)

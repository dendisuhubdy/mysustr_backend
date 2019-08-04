import redis

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

redis_image = redis.StrictRedis(host="localhost", port=6379, db=0)

class DisplayImage(Resource):
    def get(self):
        b64 = redis_image.get("image")
        b64 = b64.decode("utf-8")
        return b64

api.add_resource(DisplayImage, '/')

if __name__ == '__main__':
    app.run(debug=True, port=5555)

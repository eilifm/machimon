from flask import Flask, request
from flask_restful import Resource, Api
import ujson
import uuid
import time

app = Flask(__name__)
api = Api(app)


def make_event(data):
    ts = int(time.time()*1000000)
    uid = str(uuid.uuid4())
    data = ujson.loads(data)

    return {"ts": ts, "id": uid, "data": data}

LINES = {"data": []}

class PostAnything(Resource):
    def post(self):
        if request.data:
            event = make_event(request.data)
            LINES["data"].append(ujson.dumps(event) + "\n")
            if len(LINES["data"]) > 1000:
                with open("log.json", "a") as log:
                    log.writelines(LINES["data"])

                LINES["data"] = []
            return {"id": event['id'], "ts": event['ts']}
        else:
            return {"id": None, "ts": int(time.time() * 1000000)}

api.add_resource(PostAnything, '/post')

if __name__ == '__main__':
    app.run(debug=True, port=5001)

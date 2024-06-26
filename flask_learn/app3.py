import flask
from flask import Flask, request
import json

def run_flask(port: int, debug=True):
    app = Flask(__name__)

    @app.route("/test", methods=["POST"])
    def test():
        print(request.method)
        if request.method == "POST":
            request_data = request.get_data()
            print(request_data)
            request_data_dict = json.loads(request_data)
            print(request_data_dict)
            return json.dumps(request_data_dict)

    @app.route("/test1", methods=["POST"])
    def test1():
        print(request.method)
        if request.method == "POST":
            request_data = request.get_data()
            print(request_data)
            request_data_dict = json.loads(request_data)
            print(request_data_dict)
            request_data_dict["ret"] = "ret msg"
            return json.dumps(request_data_dict)

    app.run(port=port, debug=debug)

if __name__ == "__main__":
    run_flask(6666)

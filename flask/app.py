import flask
from flask import Flask, request
import json

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


if __name__ == "__main__":
    app.run(port="6666", debug=True)

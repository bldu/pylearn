import flask
from flask import Flask, request
import json
import time

app = Flask(__name__)

@app.route("/test", methods=["POST"])
def test():
    if request.method == "POST":
        request_data = request.get_data()
        print(request_data)
        request_data_dict = json.loads(request_data)
        print(request_data_dict)
        global is_first, last_time
        if is_first:
            print("first")
            is_first = False
            last_time = time.time()
        else:
            print("not first")
            if time.time() - last_time > 10:
                print("time exceeds 10s")
                last_time = time.time()

        return json.dumps(request_data_dict)


def main():
    global is_first
    is_first = True
    app.run(port="6666", debug=True)


if __name__ == "__main__":
    main()

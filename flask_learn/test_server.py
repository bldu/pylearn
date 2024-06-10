import requests
import json

def test_server():
    data = {"name": "nihao"}
    r = requests.post("http://127.0.0.1:6666/test", data=json.dumps(data))
    print(r.text)

    # data = {"name": "nihao"}
    # r = requests.post("http://127.0.0.1:6666/test", data=data)
    # print(r.text)

    data = '{"name": "nihao"}'
    r = requests.post("http://127.0.0.1:6666/test", data=data)
    print(r.text)


def main():
    test_server()

if __name__ == "__main__":
    main()

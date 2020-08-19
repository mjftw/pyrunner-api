from flask import Flask, Response

app = Flask(__name__)


@app.route('/run/python', methods=['POST'])
def run_python():
    return Response('', 200)

from flask import Flask, jsonify, request

from ..runner.pyrunner import PyRunner

app = Flask(__name__)


@app.route('/run/python', methods=['POST'])
def run_python():
    runner = PyRunner()
    code = request.data
    result = runner.run(code)

    print(code, result)

    return jsonify({'stdout': result.stdout, 'stderr': ''})

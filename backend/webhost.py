from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/match')
def predict():
    twitter_handle1 = request.args.get('handle1')
    twitter_handle2 = request.args.get('handle2')
    r = make_response(jsonify("todo : \"all\"")) # Raw output (including error, success and data field)
    r.headers.set('Access-Control-Allow-Origin', '*')
    return r


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

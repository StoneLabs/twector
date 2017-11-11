from flask import Flask, request, jsonify, make_response
from scipy import spatial
import subprocess
import numpy as np

app = Flask(__name__)

def getVecForHandle(handle):
    #Get tweet string
    cmd = ["ruby", "twitter-api/tweets.rb", handle]
    prc = subprocess.run(cmd, stdout=subprocess.PIPE, input="")
    tweetdata = prc.stdout.decode('utf-8')[:1000]

    print("Loading tweets...")
    #print(tweetdata)

    cmd = ["/bin/bash", "vectorizerWrapper", tweetdata]
    prc = subprocess.run(cmd, stdout=subprocess.PIPE, input="")
    raw_values = prc.stdout.decode('utf-8')[:-1]

    print("Calculating matrix...")
    #print(raw_values)

    #Split by lines to get tweets, then by space to get elements (second dimension)
    #Remove the first element (word) and convert each element of this sublist to ints
    data_lines = raw_values.split("\n")
    data_matrix = [line.split(" ")[1:-1] for line in data_lines]
    data_matrix_float = [[float(y) for y in x] for x in data_matrix]
    print(data_matrix_float)
    raw_elements = np.array(data_matrix_float)
    data_average = raw_elements.mean(axis=0) # Mean over the first dimension (vertical)

    return data_average



@app.route('/match')
def predict():
    twitter_handle1 = request.args.get('handle1')
    twitter_handle2 = request.args.get('handle2')

    vec1 = getVecForHandle(twitter_handle1)
    vec2 = getVecForHandle(twitter_handle2)

    cossim = spatial.distance.cosine(vec1, vec2)

    #todo: get tweets 1 u. 2
    #todo: calc and avrg vectors
    
    json_struct = {"math_rate: " : cossim}

    r = make_response(jsonify(json_struct)) # Raw output (including error, success and data field)
    r.headers.set('Access-Control-Allow-Origin', '*')
    return r


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

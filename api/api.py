#!flask/bin/python
# Web server
from flask import Flask
import pandas as pd
import numpy as np
import seaborn as sns
from pylab import rcParams
import base64
import json

from keras.layers.recurrent import LSTM
from keras.models import Sequential, load_model, save_model
# Get request parameters
from flask import request
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from pickle import load

# API server
app = Flask(__name__)

graph = tf.get_default_graph()

sns.set(style='whitegrid', palette='muted', font_scale=1.5)

rcParams['figure.figsize'] = 14, 8

RANDOM_SEED = 42

model = load_model("../model/model_01.h5")

x_scaler = load(open(r"../model/x_scaler.pkl", "rb"))

y_scaler = load(open(r"../model/y_scaler.pkl", "rb"))

@app.route('/getstock/<title>', methods=['GET'])
def getSearch(title):
    return title

@app.route('/getstock01/<a>/<b>', methods=['GET'])
def getSearch01(a, b):
    print(a)
    return a+b

def StockPricePredictWithModel(open, low, high, volumn):

    a = pd.DataFrame(list(zip(open, low, high, volumn, open)), columns=['open', 'low', 'high', 'volume', 'close'])

    Y = a[['close']]
    X = a[['open', 'low', 'high', 'volume']]

    X[['open', 'low', 'high', 'volume']] = x_scaler.transform(X)
    Y = y_scaler.transform(Y)

    X['close'] = Y
    X = X.values

    X = np.reshape(X, (X.shape[0], 1, X.shape[1]))

    with graph.as_default():
       res = y_scaler.inverse_transform(model.predict(X))

    res1 = []
    for t in np.nditer(res, order='F'):
        res1.append(t.item(0))

    return json.dumps(res1)


#convert list to base64 string
def Encode(lst):

    res = ''
    #list to json string
    res = json.dumps(lst)

    #Encode string to base64

    sample_string = res
    sample_string_bytes = sample_string.encode("ascii")

    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")

    return base64_string

#convert str to list
def Decode(str):
    base64_string = str
    base64_bytes = base64_string.encode("ascii")

    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")

    lst = json.loads(sample_string)

    return lst

@app.route('/getStockPrice/<open>/<low>/<high>/<volumn>/<close>', methods=['GET'])
#http://localhost:1234/getStockPrice/WzMxMi4zMDQ5NDgsIDMxMi4zMDQ5NDhd/WzMxMC45NTUwMDEsIDMxMC45NTUwMDFd/WzMxMy41ODAxNTgsIDMxMy41ODAxNThd/WzM5MjcwMDAuMCwgMzkyNzAwMC4wXQ==/WzMxMi4zMDQ5NDgsIDMxMi4zMDQ5NDhd
def StockPricePredictWithList(open, low, high, volumn,close):

    lOpen = Decode(open)
    lLow = Decode(low)
    lHigh = Decode(high)
    lVolum = Decode(volumn)
    lClose = Decode(close)

    res = StockPricePredictWithModel(lOpen, lLow, lHigh, lVolum)

    return res


# Main app
if __name__ == '__main__':
    app.run(port=1234, host='localhost', debug=True)

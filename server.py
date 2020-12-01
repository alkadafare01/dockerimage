import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle as pickle

app=Flask(__name__)
with open('model.pickle', 'rb') as f:
    print("open")
    __model = pickle.load(f)
    print(__model)
@app.route('/', methods = ["GET","POST"])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = __model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))
    #return "home.html"
if __name__ == "__main__":

    app.run(debug='TRUE')
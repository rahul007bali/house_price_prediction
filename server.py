from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names',methods=['GET'])
def get_location_names():
    responses = jsonify({
        "locations": util.get_location_names()
    })
    responses.headers.add('Access-control-Allow-Origin', '*')
    return responses


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    responses = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    responses.headers.add('Access-Control-Allow-Origin', '*')
    return responses

if __name__ == '__main__':
    print("Starting Python Flask server for home price prediction...")
    util.load_saved_artifacts()
    app.run()

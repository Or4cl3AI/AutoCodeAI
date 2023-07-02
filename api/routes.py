from flask import Flask, render_template, request, jsonify
from app.model.predict import predict_output

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def get_prediction():
    input_data = request.form['input']
    output = predict_output(input_data)
    response = {
        'output': output,
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
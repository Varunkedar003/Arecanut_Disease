from flask import Flask, render_template, request
from disease_model import predict_disease
from utils import create_pie_chart, create_bar_chart

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect form data
    features = {
        'leaf_color': request.form['leaf_color'],
        'spot_color': request.form['spot_color'],
        'leaf_texture': request.form['leaf_texture'],
        'stem_condition': request.form['stem_condition'],
        'soil_type': request.form['soil_type'],
        'moisture_level': request.form['moisture_level']
    }

    # Get prediction and confidence from model
    prediction, confidence = predict_disease(features)
    
    # Create charts
    pie_chart = create_pie_chart(confidence)
    bar_chart = create_bar_chart(features)

    # Pass all data to template
    return render_template(
        'result.html', 
        prediction=prediction, 
        confidence=confidence,
        features=features,
        pie_chart=pie_chart, 
        bar_chart=bar_chart
    )

if __name__ == '__main__':
    app.run(debug=True)
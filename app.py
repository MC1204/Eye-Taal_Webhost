import csv
import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/api/csv-data')
def get_csv_data():
    try:
        # Use os.path to ensure correct file path across environments
        csv_path = os.path.join(os.path.dirname(__file__), 'reversed_bulletin_forecast.csv')
        with open(csv_path, 'r') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)
            data = [row for row in csv_reader]
            return jsonify({
                'success': True,
                'headers': headers,
                'data': data
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

# Add this for Vercel deployment
@app.route('/api/health')
def health_check():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)
import csv
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/api/csv-data')
def get_csv_data():
    try:
        with open('reversed_bulletin_forecast.csv', 'r') as file:
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

if __name__ == '__main__':
    app.run(debug=True)
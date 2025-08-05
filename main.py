from flask import Flask, request, jsonify
import yfinance as yf
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/quote', methods=['GET'])
def quote():
    ticker = request.args.get('ticker')
    period = request.args.get('period', '5d')
    interval = request.args.get('interval', '1d')

    if not ticker:
        return jsonify({"error": "Ticker ist erforderlich"}), 400

    try:
        data = yf.Ticker(ticker).history(period=period, interval=interval)
        return jsonify(data.reset_index().to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

from flask import Flask, jsonify
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/api/data')
def get_data():
    count = cache.incr('hits')
    return jsonify({"message": "Hello Docker!", "count": count})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

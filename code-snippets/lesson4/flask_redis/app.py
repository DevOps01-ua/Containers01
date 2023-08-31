from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = cache.incr('hits')
    return 'Hello Docker! This page has been viewed {} times.\n'.format(count)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

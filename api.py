#!/usr/bin/env python3
"""
flask app
"""
from flask import Flask, jsonify, request
from datetime import datetime


app = Flask(__name__)


@app.route('/', methods=['GET'])
def user():
    """ getting some query """
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    dt = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    current_day = datetime.now().strftime('%A')
    status_code = 200

    response_data = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': dt,
        'track': track,
        'github_file_url': 'https://github.com/Olatundeawo/HGNX/blob/main/api.py',
        'github_repo_url': 'https://github.com/Olatundeawo/HGNX',
        'status_code': status_code
    }

    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)
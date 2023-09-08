#!/usr/bin/env python3
"""
python script
"""
from flask import Flask, jsonify, request
from datetime import datetime


app = Flask(__name__)


@app.route('/', methods=['GET'])
def user():
    """ getting some query """
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    # get current datetime
    dt = datetime.now()
    # get the current day
    current_day = dt.strftime('%A')
    status_code = 200

    response_data = {
        'slack_name': slack_name,
        'current_day': current_day,
        # 'utc_time': utc_time,
        'track': track,
        # 'github_file_url': github_file_url,
        # 'github_repo_url': github_repo_url,
        # 'status_code': status_code
    }

    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)
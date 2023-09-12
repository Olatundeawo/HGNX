#!/usr/bin/env python3
"""
flask app
"""
from flask import Flask, request, Response
from datetime import datetime
import json
from collections import OrderedDict


app = Flask(__name__)


@app.route('/api', methods=['GET'])
def user():
    """ getting some query """
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    dt = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    current_day = datetime.now().strftime('%A')
    status_code = 200
    
    response_data = OrderedDict()
    response_data['slack_name'] = slack_name
    response_data['current_day'] = current_day
    response_data['utc_time'] = dt
    response_data['track'] = track
    response_data['github_file_url'] = 'https://github.com/Olatundeawo/HGNX/blob/main/api.py'
    response_data['github_repo_url'] = 'https://github.com/Olatundeawo/HGNX'
    response_data['status_code'] = status_code
    
    
    json_data = json.dumps(response_data)
    
    response = Response(json_data, content_type='application/json')
    return response


if __name__ == '__main__':
    app.run(debug=True)
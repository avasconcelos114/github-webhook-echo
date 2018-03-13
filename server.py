#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, abort, request 
import json

app = Flask(__name__)

@app.route('/receiveHook', methods=['POST']) 
def receiveHook():
    event = request.headers.get('X-GitHub-Event') # Information on event is received in the header
    data = request.json # Payload with relevant data
    print_data_yn = False # Change this value to `True` to print payload to console

    if not data:
        abort(400)
    
    print 'Event name: ' + event
    if 'organization' in data:
        print 'Organization: ' + data['organization']['login']

    # Print events related to `Member`
    if event == 'member':
        if data['action'] == 'created':
            print 'A new Collaborator has been added.'
        if data['action'] == 'deleted':
            print 'A Collaborator has been deleted.'
    
    # Print events related to `Organization` (only available on Enterprise versions)
    if event == 'organization':
        if data['action'] == 'created':
            print 'A new organization has been added.'
        if data['action'] == 'member_added': 
            print 'A new member has been added to an organization.'
        if data['action'] == 'member_removed': 
            print 'A member has been deleted from an organization.'
    
    if print_data_yn:
        print json.dumps(request.json)

    return json.dumps(request.json)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, abort, request 
import json

app = Flask(__name__)

@app.route('/receiveHook', methods=['POST']) 
def receiveHook():
    event = request.headers.get('X-GitHub-Event') # Event 정보
    data = request.json # Payload
    print_data_yn = False # Request를 콘솔로 print 하려면 True 값으로 수정

    if not data:
        abort(400)
    
    print 'Event name: ' + event
    print 'Organization: ' + data['organization']['login']
    # Member관련 Event를 print
    if event == 'member':
        if data['action'] == 'created':
            print 'A new collaborator has been added!'
        if data['action'] == 'deleted':
            print 'A collaborator has left the repository! :('
    
    # Org 관련 Event를 print
    if event == 'organization':
        if data['action'] == 'created': # ORG 생성 감지
            print 'An organization has been created, this is where you send MChat a request!'
        if data['action'] == 'member_added': # ORG 멤버 추가 감지
            print 'a member was added to the organization!'
        if data['action'] == 'member_removed': # ORG 멤버 삭제 감지
            print 'a member was REMOVED from the organization!'
    
    if print_data_yn:
        print json.dumps(request.json)

    return json.dumps(request.json)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

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
    if 'organization' in data:
        print 'Organization: ' + data['organization']['login']

    # Member관련 Event를 print
    if event == 'member':
        if data['action'] == 'created':
            print '신규 Collaborator 추가되었습니다.'
        if data['action'] == 'deleted':
            print 'Collaborator가 삭제되었습니다.'
    
    # Org 관련 Event를 print
    if event == 'organization':
        if data['action'] == 'created': # ORG 생성 감지
            print '신규 organization 추가되었습니다.'
        if data['action'] == 'member_added': # ORG 멤버 추가 감지
            print 'organization 멤버 추가되었습니다.'
        if data['action'] == 'member_removed': # ORG 멤버 삭제 감지
            print 'organization 멤버 삭제되었습니다.'
    
    if print_data_yn:
        print json.dumps(request.json)

    return json.dumps(request.json)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

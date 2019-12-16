from flask import Flask
from flask import request
import secrets

app = Flask(__name__)

@app.route('/AuthAPIKey', methods=['POST'])
def authApi():
    content = request.data.decode('UTF-8')
    print(content)
    if content == 'bHeKgNkRnTqWtYv3y5A7DaFcHfMhPkSp' or content == '5A7DaFcHfMhPmSpUrXuZw3z6B8DbGdJg' or content == 'A7DaFcJfMhPmSpUrXuZw3z6B8EbGdJgN':
       response = {'message': 'Authentication successful!', 'session_token': secrets.token_urlsafe()}
       return response, 200
    else:
        response = {'message': 'Invalid API key!', 'session_token': ''}
        return response, 401

@app.route('/AuthUserPass', methods=['POST'])
def authUser():
    content = request.json
    if ((content['username'] == 'evan' and content['password'] == 'Cyb3r@rk1') or (content['username'] == 'rob' and content['password'] == 'CyberArk2!')):
        response = {'message': 'Authentication successful!', 'session_token': secrets.token_urlsafe()}
        return response, 200
    else:
        response = {'message': 'Failed to authenticate with given username and password!', 'session_token': ''}
        return response, 401

if __name__ == '__main__':
    app.run(host='0.0.0.0')

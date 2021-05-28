import binascii
import json
import os
from flask import Flask, jsonify, abort,  request
import hashlib
import datetime

app = Flask(__name__)

try:
    with open('users.json', 'r') as json_file:
        users = json.load(json_file)
except FileNotFoundError:
    users = []
    with open('users.json', 'w') as json_file:
        json.dump(users, json_file)

def hashing(password):
    salt = hashlib.sha256(os.urandom(70)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 80000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = list(filter(lambda x: x['id'] == user_id, users))
    if len(user) == 0:
        abort(404)
    return jsonify({'users': user[0]})

@app.route('/users/<string:user_login>', methods=['GET'])
def get_user_by_login(user_login):
    user = list(filter(lambda x: x['login'] == user_login, users))
    if len(user) == 0:
        abort(404)
    return jsonify({'users': user[0]})

@app.route('/user', methods=['POST'])
def create_user():
    try:
        user_new = {
            'id': users[-1]['id'] + 1,
            'login': request.json['login'],
            'password': hashing(str(request.json['password'])),
            'regDate': datetime.datetime.now().isoformat()
        }
        users.append(user_new)
        with open('users.json', 'w') as json_file:
            json.dump(users, json_file)
        return jsonify({'user': user_new}), 201
    except IndexError:
        user_new = {
            'id': 1,
            'login': request.json['login'],
            'password': hashing(request.json['password']),
            'regDate': datetime.datetime.now().isoformat()

        }
        users.append(user_new)
        with open('users.json', 'w') as json_file:
            json.dump(users, json_file)
        return jsonify({'user': user_new}), 201
    except:
        abort(400)

@app.route('/user', methods=['GET'])
def get_users():
    return jsonify({"users": users})

if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')
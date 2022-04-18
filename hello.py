
from flask import Flask, jsonify
from flask import make_response
from flask import abort
from flask import request


app = Flask(__name__)

'''
A trivial Flask Application with routes
'''
friends = [ ]

@app.route('/',methods=['GET'])
def hello_world():
    return 'Hello World!', 200


@app.route('/<name>',methods=['GET'])
def hello_peep(name):
    return f'Hello {name}!', 200

@app.route('/friends',methods=['GET'])
def hello_friends():
    return jsonify({'friends': friends}), 200

@app.route('/add/<name>',methods=['POST'])
def add_peep(name):
    index = len(friends)
    friend = {
        'id': index,
        'name': name
    }
    friends.append(friend)
    return jsonify({'id': friend['id'], 'friend': friend}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

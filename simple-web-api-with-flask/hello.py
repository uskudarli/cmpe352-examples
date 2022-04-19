from flask import Flask, jsonify

app = Flask(__name__)

'''
A trivial Flask Application with routes
'''
friends = []

'''
A base call that simply returns the text Hello World
method: GET
status code: 200
'''
@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!', 200

'''
A call that  returns Hello followed by 'name'
method: GET
status code: 200
'''
@app.route('/<name>', methods=['GET'])
def hello_peep(name):
    return f'Hello {name}!', 200

'''
A  call that  returns list of friends as JSON
method: GET
status code: 200
'''
@app.route('/friends', methods=['GET'])
def hello_friends():
    return jsonify({'friends': friends}), 200

'''
A  call that adds 'name' to friends and returns added friend as JSON
method: POST
status code: 200
'''
@app.route('/add/<name>', methods=['POST'])
def add_peep(name):
    index = len(friends)
    friend = {
        'id': index,
        'name': name
    }
    friends.append(friend)
    return jsonify({'id': friend['id'], 'friend': friend}), 201

'''
Main function
'''
if __name__ == '__main__':
    app.run()

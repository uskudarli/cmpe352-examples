from flask import Flask, jsonify, render_template


app = Flask(__name__)

'''
A trivial Flask Application that uses HTML templates for UI
'''
friends = []

'''
A  call that returns Hello World. 
Returns HTML with blue text (see color)
otherwise used simple text.
Method: GET
'''
@app.route('/', methods=['GET'])
def hello_world():
    return render_template('hello_template.html', color="blue"), 200

'''
A  call that returns Hello followed by 'name' . 
Returns HTML in purple text.
Method: GET
'''
@app.route('/<name>', methods=['GET'])
def hello_peep(name):
    return render_template('hello_peep.html', peep=name, color="purple"), 200

'''
A  call that  returns list of friends as JSON
method: GET
status code: 200
QUESTION: How could you use a nice template to show the friends?
'''
@app.route('/friends', methods=['GET'])
def hello_friends():
    return jsonify({'friends': friends}), 200

'''
A  call that adds 'name' to friends and returns added friend as JSON
method: POST
status code: 200
QUESTION: How could you use a nice template to show the newly added friend?

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


if __name__ == '__main__':
    app.run()

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

'''
A trivial Flask Application that uses HTML templates for UI
'''
friends = []

'''
A base function that presents a form for entering a name as HTML
Method: GET
'''
@app.route('/', methods=['GET'])
def hello_world():
    return render_template('hello_buttons_template.html', color="blue"), 200

'''
A base function that returns Hello to peep (obtained from form) 
Returns HTML
Method: POST
'''
@app.route("/", methods=['POST'])  # could add GET method to handle both cases
def index():
    name = request.form.get('peep')
    print(name)
    return render_template('hello_peep.html', peep=name, color="purple"), 200


if __name__ == '__main__':
    app.run(debug=True)

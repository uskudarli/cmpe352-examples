from flask import Flask, render_template
import os

app = Flask(__name__)

'''
A base call that returns a random photo from picsum. 
Returns HTML
Method: GET (remember: it is default, here it is not shown explicitly)
The hello_images.html file provides CSS in template header. 
'''
@app.route("/")
def index():
    url = 'https://picsum.photos/400'
    return render_template("hello_images.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return 'THI IS WORKING'

if __name__ == '__main__':
    app.run(debug=True)
 
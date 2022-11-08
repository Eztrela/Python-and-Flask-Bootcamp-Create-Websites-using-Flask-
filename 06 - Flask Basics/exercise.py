from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'<h1>Welcome! Go to /puppy_latin/name to see yout name in puppy latin!</h1>'

@app.route('/puppy_latin/<name>')
def puppy(name):
    if name[-1] is 'y':
        return f'<h1>Hi {name}! Your puppylatin name is {name[:len(name) - 1] + "iful"}</h1>'
    else:
        return f'<h1>Hi {name}! Your puppylatin name is {name[:len(name)] + "y"}</h1>'

if __name__ == '__main__':
    app.run()
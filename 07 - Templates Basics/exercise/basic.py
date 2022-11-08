from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    name = request.args.get('name')
    result = []

    has_lower = any(char.islower() for char in name)
    if not has_lower:
        result.append('You did not user an lowercase character')


    has_upper = any(char.isupper() for char in name)
    if not has_upper:
        result.append('You did not user an  uppercase character')

    
    has_digit = name[-1].isdigit()
    if not has_digit:
        result.append('You did not end your username with a number')

    return render_template('report.html', result = result)

if __name__ == '__main__':
    app.run(debug=True)
 
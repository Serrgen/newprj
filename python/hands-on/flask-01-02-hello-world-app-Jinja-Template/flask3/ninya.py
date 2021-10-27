from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html' , number1 = 12, number2 =123)

@app.route('/mult')
def num():
    v1, v2 = 14, 223
    return render_template('body.html', value1 = v1, value2 = v2, value3 = v1*v2)


if __name__ == '__main__':
    app.run(debug=True)
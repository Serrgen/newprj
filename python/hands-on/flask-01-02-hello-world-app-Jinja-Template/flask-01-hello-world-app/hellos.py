from flask import Flask

app = Flask(__name__)

@app.route('/')
def hellos():
    return  "hellos world"

@app.route('/second')
def sec():
    return "yaannii"

@app.route('/forth/<string:id>')
def forth(id):
    return f'id num is {id}'



if __name__ == '__main__':
    app.run(debug=True, port=2000)
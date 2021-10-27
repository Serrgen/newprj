from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def homa():
    return 'This is ipek page, <h1> Welcome home </h1>'

@app.route('/error')
def error():
    return '<h1> error page </h1>'

@app.route('/hello')
def hello():
    return f'<h1> HELLO WORLD </h1>'


@app.route('/admin')
def admin():
    return redirect(url_for('error'))



@app.route('/<name>')
def greet(name):
    greet_format = f''' 
<!DOCTYPE html>
<html>
<head>
    <title>Greeting Page</title>
</head>
<body>
    <h1>Hello, { name }!</h1>
    <h1>Welcome to my Greeting Page</h1>
</body>
</html>
    '''
    return greet_format

@app.route('/greet_admin')
def greet_admin():
    return redirect(url_for('greet', name = 'master admin'))


@app.route('/evenns')
def head():
    names = "orhan"
    return render_template('greet.html', name = names)


#@app.route('/serhen')

#def mylist():
    #names =["arif", "salih", "erkan"]
    #return render_template('greet.html', range(1,11)=names)



if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=80)
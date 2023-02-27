from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route("/test")
def test():
    return template('<h1>HI</h1>')

run(host='localhost', port=8080)
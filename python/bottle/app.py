from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route("/test")
def test():
    return template()

run(host='localhost', port=8080)
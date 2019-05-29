from app import app

#route is a decorator function defined in the Flask class
@app.route('/')
@app.route('/index')
def index():
    return "Hello World"

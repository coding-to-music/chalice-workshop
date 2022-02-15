from chalice import Chalice

app = Chalice(app_name='workshop-intro')


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/hello')
def hello_workshop():
    return {'hello': 'workshop'}

@app.route('/hello/{name}')
def hello_name(name):
    return {'hello': name}

@app.route('/hello-post', methods=['POST'])
def hello_post():
    request_body = app.current_request.json_body
    return {'hello': request_body}
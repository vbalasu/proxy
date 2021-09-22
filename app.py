from chalice import Chalice, Response

app = Chalice(app_name='proxy')


@app.route('/', methods=['GET'])
def index():
    import requests
    # It is assumed that the url will be encoded. Use Javascript's encodeURIComponent function
    url = app.current_request.query_params['url']
    method = app.current_request.method
    if method == 'GET':
        response = requests.get(url)
        return Response(body=response.text, status_code=response.status_code, headers={'Content-Type': response.headers['Content-Type']})
    else:
        return f'Unsupported method: {method}'


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#

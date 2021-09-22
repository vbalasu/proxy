from chalice import Chalice, Response

app = Chalice(app_name='proxy')

# USAGE - local: curl "http://127.0.0.1:8000/?url=https%3A%2F%2Fapi.coingecko.com%2Fapi%2Fv3%2Fsimple%2Fprice%3Fvs_currencies%3Dusd%26ids%3Dalgorand%2Cbinancecoin%2Cbitcoin%2Ccardano%2Cethereum%2Cpolkadot%2Csolana%2Cwrapped-bitcoin%2Cuniswap%2Cgitcoin"
# USAGE - lambda: curl "https://mri8t8njf1.execute-api.us-east-1.amazonaws.com/api/?url=https%3A%2F%2Fapi.coingecko.com%2Fapi%2Fv3%2Fsimple%2Fprice%3Fvs_currencies%3Dusd%26ids%3Dalgorand%2Cbinancecoin%2Cbitcoin%2Ccardano%2Cethereum%2Cpolkadot%2Csolana%2Cwrapped-bitcoin%2Cuniswap%2Cgitcoin"
# USAGE - production: curl "https://proxy.cloudmatica.com/?url=https%3A%2F%2Fapi.coingecko.com%2Fapi%2Fv3%2Fsimple%2Fprice%3Fvs_currencies%3Dusd%26ids%3Dalgorand%2Cbinancecoin%2Cbitcoin%2Ccardano%2Cethereum%2Cpolkadot%2Csolana%2Cwrapped-bitcoin%2Cuniswap%2Cgitcoin"
@app.route('/', methods=['GET'])
def index():
    import requests
    # It is assumed that the url will be encoded. Use Javascript's encodeURIComponent function
    url = app.current_request.query_params['url']
    method = app.current_request.method
    if method == 'GET':
        print(url)
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

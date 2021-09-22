# proxy

This is a generic proxy server implemented using AWS Lambda.

Any request that is made to the proxy endpoint (https://proxy.cloudmatica.com?url=https://example.com) is forwarded, and the response is sent back with the fewest modifications possible.

Currently, only GET requests are supported.

USAGE:

`curl "https://proxy.cloudmatica.com/?url=https%3A%2F%2Fapi.coingecko.com%2Fapi%2Fv3%2Fsimple%2Fprice%3Fvs_currencies%3Dusd%26ids%3Dalgorand%2Cbinancecoin%2Cbitcoin%2Ccardano%2Cethereum%2Cpolkadot%2Csolana%2Cwrapped-bitcoin%2Cuniswap%2Cgitcoin"`

or just use the browser

[https://proxy.cloudmatica.com/?url=https%3A%2F%2Fapi.coingecko.com%2Fapi%2Fv3%2Fsimple%2Fprice%3Fvs_currencies%3Dusd%26ids%3Dalgorand%2Cbinancecoin%2Cbitcoin%2Ccardano%2Cethereum%2Cpolkadot%2Csolana%2Cwrapped-bitcoin%2Cuniswap%2Cgitcoin](https://proxy.cloudmatica.com/?url=https%3A%2F%2Fapi.coingecko.com%2Fapi%2Fv3%2Fsimple%2Fprice%3Fvs_currencies%3Dusd%26ids%3Dalgorand%2Cbinancecoin%2Cbitcoin%2Ccardano%2Cethereum%2Cpolkadot%2Csolana%2Cwrapped-bitcoin%2Cuniswap%2Cgitcoin)
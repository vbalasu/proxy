# proxy

This is a generic proxy server implemented using AWS Lambda.

Any request that is made to the proxy endpoint (https://proxy.cloudmatica.com?url=https://example.com) is forwarded, and the response is sent back with the fewest modifications possible.
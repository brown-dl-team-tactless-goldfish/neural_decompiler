import requests

# set up the Compiler Explorer API endpoint
url = 'https://godbolt.org/api/compiler/g82/compile'

# set up the request headers
headers = {'Content-type': 'application/json'}

# set up the C code snippet to be compiled
code = 'int main() { return 0; }'

# set up the request body
data = {
    'source': code,
    'options': {
        'filters': {
            "intel": False
        }
    }
}

# send the POST request
response = requests.post(url, headers=headers, json=data)

# retrieve the resulting assembly or binary code
if response.ok:
    result = response.text
else:
    result = f'Error {response.status_code}: {response.reason}'

print(result)
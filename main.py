import requests

response = requests.get('https://httpbin.org/basic-auth/user/passwd', auth=('user', 'passwd'))
print(response)

print(response.json())
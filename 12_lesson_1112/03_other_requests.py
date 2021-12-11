import requests

url = 'https://httpbin.org/'
post = requests.post(url + 'post',
                     data={'name': 'GreatRaksin',
                           'password': '12345qwerty'})

print(post.json())


